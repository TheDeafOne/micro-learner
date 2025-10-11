from __future__ import annotations

if __name__ == "__main__" and __package__ is None:  # pragma: no cover - script setup
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent))
    __package__ = "backend"

from datetime import datetime

from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException
from sqlmodel import Session, select

from backend.canvas_client import CanvasClient
from backend.deps import get_engine, get_session, init_db
from backend.models import Artifact, Course, Item, ItemStatus, Module
from backend.providers import infer_provider_from_url, normalize_provider_url, resolve_provider
from backend.schemas import (
    ArtifactRead,
    CourseRead,
    ItemDetail,
    ItemRead,
    ModuleRead,
    RefreshResult,
)
from backend.settings import Settings, get_settings
from backend.storage import ensure_data_dirs, transcript_path, write_summary, write_transcript
from backend.summarizer import summarize_transcript


app = FastAPI(title="Canvas Summarization Backend")


@app.on_event("startup")
def on_startup() -> None:
    settings = get_settings()
    init_db()
    ensure_data_dirs(settings)


@app.get("/health")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/me/courses", response_model=list[CourseRead])
def list_courses(session: Session = Depends(get_session)) -> list[Course]:
    statement = select(Course).order_by(Course.name)
    return session.exec(statement).all()


@app.post("/me/courses/refresh", response_model=RefreshResult)
async def refresh_courses(
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
) -> RefreshResult:
    async with CanvasClient(settings) as client:
        courses_data = await client.fetch_courses()
    now = datetime.utcnow()
    updated = 0
    for payload in courses_data:
        course_id = payload.get("id")
        if course_id is None:
            continue
        name = payload.get("name") or payload.get("course_code") or f"Course {course_id}"
        course = session.get(Course, course_id)
        if course:
            course.name = name
            course.last_synced_at = now
        else:
            course = Course(id=course_id, name=name, last_synced_at=now)
            session.add(course)
        updated += 1
    session.commit()
    detail = "Courses refreshed from Canvas" if updated else "No courses returned from Canvas"
    return RefreshResult(count=updated, detail=detail)


@app.get("/courses/{course_id}", response_model=CourseRead)
def get_course(course_id: int, session: Session = Depends(get_session)) -> Course:
    course = session.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@app.get("/courses/{course_id}/modules", response_model=list[ModuleRead])
def list_modules(course_id: int, session: Session = Depends(get_session)) -> list[Module]:
    if not session.get(Course, course_id):
        raise HTTPException(status_code=404, detail="Course not found")
    statement = (
        select(Module)
        .where(Module.course_id == course_id)
        .order_by(Module.position, Module.title)
    )
    return session.exec(statement).all()


@app.post("/courses/{course_id}/modules/refresh", response_model=RefreshResult)
async def refresh_modules(
    course_id: int,
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
) -> RefreshResult:
    course = session.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    now = datetime.utcnow()
    module_count = 0
    item_count = 0

    async with CanvasClient(settings) as client:
        modules_data = await client.fetch_modules(course_id)
        for module_payload in modules_data:
            module_id = module_payload.get("id")
            if module_id is None:
                continue
            title = module_payload.get("name") or module_payload.get("title") or f"Module {module_id}"
            position = module_payload.get("position")

            module = session.get(Module, module_id)
            if module:
                module.title = title
                module.position = position
                module.last_synced_at = now
            else:
                module = Module(
                    id=module_id,
                    course_id=course_id,
                    title=title,
                    position=position,
                    last_synced_at=now,
                )
                session.add(module)
            module_count += 1

            items_payload = await client.fetch_module_items(course_id, module_id)
            for item_payload in items_payload:
                item_id = item_payload.get("id")
                if item_id is None:
                    continue
                item = session.get(Item, item_id)
                title = item_payload.get("title") or item_payload.get("name") or f"Item {item_id}"
                item_type = item_payload.get("type")
                html_url = item_payload.get("html_url") or item_payload.get("url")
                provider = infer_provider_from_url(html_url)
                normalized_url = normalize_provider_url(provider, html_url)

                if item:
                    item.title = title
                    item.type = item_type
                    item.canvas_url = normalized_url or html_url
                    item.provider = provider or item.provider
                    item.last_synced_at = now
                else:
                    item = Item(
                        id=item_id,
                        module_id=module_id,
                        title=title,
                        type=item_type,
                        canvas_url=normalized_url or html_url,
                        provider=provider,
                        status=ItemStatus.DISCOVERED,
                        last_synced_at=now,
                    )
                    session.add(item)
                item_count += 1

    course.last_synced_at = now
    session.add(course)
    session.commit()
    detail = f"Modules synced: {module_count}; items synced: {item_count}"
    return RefreshResult(count=module_count, detail=detail)


@app.get("/modules/{module_id}/items", response_model=list[ItemRead])
def list_items(module_id: int, session: Session = Depends(get_session)) -> list[Item]:
    if not session.get(Module, module_id):
        raise HTTPException(status_code=404, detail="Module not found")
    statement = select(Item).where(Item.module_id == module_id).order_by(Item.title)
    return session.exec(statement).all()


@app.get("/items/{item_id}", response_model=ItemDetail)
def get_item(item_id: int, session: Session = Depends(get_session)) -> ItemDetail:
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    artifacts = session.exec(select(Artifact).where(Artifact.item_id == item_id)).all()
    transcript_artifact = next((a for a in artifacts if a.kind == "transcript"), None)
    summary_artifact = next((a for a in artifacts if a.kind == "summary"), None)
    item_payload = ItemRead.model_validate(item).model_dump()
    return ItemDetail(
        **item_payload,
        transcript_path=transcript_artifact.path if transcript_artifact else None,
        summary_path=summary_artifact.path if summary_artifact else None,
        artifacts=[ArtifactRead.model_validate(a) for a in artifacts],
    )


@app.post("/items/{item_id}/fetch-transcript", response_model=dict)
def fetch_transcript(
    item_id: int,
    background_tasks: BackgroundTasks,
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
) -> dict[str, str]:
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.status = ItemStatus.DISCOVERED
    item.error = None
    session.add(item)
    session.commit()
    background_tasks.add_task(run_transcript_job, item_id, settings)
    return {"status": "queued"}


@app.post("/items/{item_id}/summarize", response_model=dict)
def summarize_item(
    item_id: int,
    background_tasks: BackgroundTasks,
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
) -> dict[str, str]:
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    transcript_file = transcript_path(item_id, settings)
    if not transcript_file.exists():
        raise HTTPException(status_code=409, detail="Transcript not ready")
    item.status = ItemStatus.TRANSCRIPT_READY
    item.error = None
    session.add(item)
    session.commit()
    background_tasks.add_task(run_summary_job, item_id, settings)
    return {"status": "queued"}


def run_transcript_job(item_id: int, settings: Settings) -> None:
    ensure_data_dirs(settings)
    engine = get_engine()
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            return
        try:
            provider = resolve_provider(item)
            transcript_text = provider.fetch(item)
            path = write_transcript(item.id, transcript_text, settings)
            artifact = session.exec(
                select(Artifact).where(Artifact.item_id == item.id, Artifact.kind == "transcript")
            ).first()
            if artifact:
                artifact.path = str(path)
                artifact.created_at = datetime.utcnow()
            else:
                artifact = Artifact(
                    item_id=item.id,
                    kind="transcript",
                    path=str(path),
                    created_at=datetime.utcnow(),
                )
                session.add(artifact)
            item.status = ItemStatus.TRANSCRIPT_READY
            item.error = None
            session.add(item)
            session.commit()
        except Exception as exc:  # pragma: no cover - background logging
            item.status = ItemStatus.FAILED
            item.error = str(exc)
            session.add(item)
            session.commit()


if __name__ == "__main__":  # pragma: no cover - convenience runner
    import uvicorn

    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)


def run_summary_job(item_id: int, settings: Settings) -> None:
    ensure_data_dirs(settings)
    engine = get_engine()
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            return
        try:
            transcript_file = transcript_path(item.id, settings)
            if not transcript_file.exists():
                raise FileNotFoundError("Transcript file missing")
            transcript_text = transcript_file.read_text(encoding="utf-8")
            summary_text = summarize_transcript(transcript_text, settings)
            path = write_summary(item.id, summary_text, settings)
            artifact = session.exec(
                select(Artifact).where(Artifact.item_id == item.id, Artifact.kind == "summary")
            ).first()
            if artifact:
                artifact.path = str(path)
                artifact.created_at = datetime.utcnow()
            else:
                artifact = Artifact(
                    item_id=item.id,
                    kind="summary",
                    path=str(path),
                    created_at=datetime.utcnow(),
                )
                session.add(artifact)
            item.status = ItemStatus.SUMMARY_READY
            item.error = None
            session.add(item)
            session.commit()
        except Exception as exc:  # pragma: no cover - background logging
            item.status = ItemStatus.FAILED
            item.error = str(exc)
            session.add(item)
            session.commit()
