from __future__ import annotations

if __name__ == "__main__" and __package__ is None:  # pragma: no cover - script setup
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent))
    __package__ = "backend"

import json
import logging
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Optional

import httpx
from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from sqlalchemy import func
from sqlmodel import Session, select

from backend.canvas_client import CanvasClient
from backend.deps import get_engine, get_session, init_db
from backend.models import Artifact, Course, Item, ItemStatus, Module
from backend.providers import (
    extract_media_entries,
    infer_provider_from_url,
    normalize_provider_url,
    resolve_provider,
)
from backend.schemas import (
    ArtifactRead,
    CourseRead,
    ItemDetail,
    ItemRead,
    MediaLink,
    ModuleRead,
    RefreshResult,
)
from backend.settings import Settings, get_settings
from backend.storage import ensure_data_dirs, transcript_path, write_summary, write_transcript
from backend.summarizer import summarize_transcript


logger = logging.getLogger(__name__)


app = FastAPI(title="Canvas Summarization Backend")


@app.on_event("startup")
def on_startup() -> None:
    settings = get_settings()
    init_db()
    ensure_data_dirs(settings)
    if not logging.getLogger().handlers:
        logging.basicConfig(level=logging.INFO)


def parse_media_entries(media_json: str | None) -> list[dict[str, str]]:
    if not media_json:
        return []
    try:
        data = json.loads(media_json)
    except json.JSONDecodeError:
        return []
    if not isinstance(data, list):
        return []
    entries: list[dict[str, str]] = []
    for entry in data:
        if not isinstance(entry, dict):
            continue
        provider = entry.get("provider")
        url = entry.get("url")
        if not provider or not url:
            continue
        entries.append({"provider": provider, "url": url})
    return entries


def format_transcript_bundle(sections: list[tuple[str, str, str]]) -> str:
    if not sections:
        return ""
    lines: list[str] = []
    for idx, (provider, url, text) in enumerate(sections, start=1):
        heading = f"## Transcript {idx} ({provider})"
        lines.append(heading)
        lines.append(f"Source: {url}")
        lines.append("")
        lines.append((text or "").strip())
        lines.append("")
    return "\n".join(lines).strip()


@app.get("/health")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


def _list_courses(session: Session) -> list[Course]:
    statement = select(Course).order_by(Course.name)
    return session.exec(statement).all()


@app.get("/courses", response_model=list[CourseRead])
def list_courses(session: Session = Depends(get_session)) -> list[Course]:
    return _list_courses(session)


@app.get("/me/courses", response_model=list[CourseRead])
def list_my_courses(session: Session = Depends(get_session)) -> list[Course]:
    return _list_courses(session)


@app.post("/me/courses/refresh", response_model=RefreshResult)
async def refresh_courses(
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
) -> RefreshResult:
    try:
        async with CanvasClient(settings) as client:
            courses_data = await client.fetch_courses()
    except httpx.HTTPStatusError as exc:
        logger.exception("Canvas returned error while fetching courses")
        raise HTTPException(
            status_code=exc.response.status_code,
            detail=f"Canvas API error while fetching courses: {exc.response.text}",
        )
    except httpx.RequestError as exc:
        logger.exception("Network error while fetching courses from Canvas")
        raise HTTPException(
            status_code=502,
            detail=f"Unable to reach Canvas API: {exc}",
        )
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


@app.get("/modules/{module_id}", response_model=ModuleRead)
def get_module(module_id: int, session: Session = Depends(get_session)) -> Module:
    module = session.get(Module, module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    return module


@app.get("/items", response_model=list[ItemRead])
def list_items_global(
    session: Session = Depends(get_session),
    course_id: Optional[int] = Query(default=None),
    module_id: Optional[int] = Query(default=None),
    status: Optional[list[ItemStatus]] = Query(default=None),
    provider: Optional[str] = Query(default=None),
    search: Optional[str] = Query(default=None),
) -> list[Item]:
    statement = select(Item)

    if module_id is not None:
        statement = statement.where(Item.module_id == module_id)
    elif course_id is not None:
        module_ids = session.exec(select(Module.id).where(Module.course_id == course_id)).all()
        if not module_ids:
            return []
        statement = statement.where(Item.module_id.in_(module_ids))

    if status:
        statement = statement.where(Item.status.in_(status))

    if provider:
        statement = statement.where(func.lower(Item.provider) == provider.lower())

    if search:
        pattern = f"%{search.lower()}%"
        statement = statement.where(func.lower(Item.title).like(pattern))

    statement = statement.order_by(Item.last_synced_at.desc(), Item.id)
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

    try:
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
                    page_url_slug = item_payload.get("page_url")
                    media_entries: list[dict[str, str]] = []

                    if item_type == "Page" and page_url_slug:
                        try:
                            page_body = await client.fetch_page_body(course_id, page_url_slug)
                        except Exception:
                            page_body = ""
                        media_entries = extract_media_entries(page_body)
                        if media_entries and not provider:
                            provider = media_entries[0]["provider"]
                    elif provider:
                        normalized_url = normalize_provider_url(provider, html_url)
                        target_url = normalized_url or html_url
                        if target_url:
                            media_entries.append({"provider": provider, "url": target_url})

                    media_json = json.dumps(media_entries) if media_entries else None

                    if item:
                        item.title = title
                        item.type = item_type
                        item.page_url = page_url_slug
                        item.canvas_url = html_url
                        item.provider = provider
                        item.media_urls = media_json
                        item.last_synced_at = now
                    else:
                        item = Item(
                            id=item_id,
                            module_id=module_id,
                            title=title,
                            type=item_type,
                            page_url=page_url_slug,
                            canvas_url=html_url,
                            provider=provider,
                            status=ItemStatus.DISCOVERED,
                            last_synced_at=now,
                            media_urls=media_json,
                        )
                        session.add(item)
                    item_count += 1
    except httpx.HTTPStatusError as exc:
        logger.exception("Canvas API error while syncing modules for course %s", course_id)
        raise HTTPException(
            status_code=exc.response.status_code,
            detail=f"Canvas API error while fetching modules/items: {exc.response.text}",
        )
    except httpx.RequestError as exc:
        logger.exception("Network error while syncing modules for course %s", course_id)
        raise HTTPException(
            status_code=502,
            detail=f"Unable to reach Canvas API: {exc}",
        )

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


@app.get("/items/{item_id}/artifacts", response_model=list[ArtifactRead])
def list_item_artifacts(item_id: int, session: Session = Depends(get_session)) -> list[Artifact]:
    if not session.get(Item, item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    statement = select(Artifact).where(Artifact.item_id == item_id).order_by(Artifact.created_at.desc())
    return session.exec(statement).all()


@app.get("/artifacts/{artifact_id}", response_model=ArtifactRead)
def get_artifact(artifact_id: int, session: Session = Depends(get_session)) -> Artifact:
    artifact = session.get(Artifact, artifact_id)
    if not artifact:
        raise HTTPException(status_code=404, detail="Artifact not found")
    return artifact


@app.get("/items/{item_id}", response_model=ItemDetail)
def get_item(item_id: int, session: Session = Depends(get_session)) -> ItemDetail:
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    artifacts = session.exec(select(Artifact).where(Artifact.item_id == item_id)).all()
    transcript_artifact = next((a for a in artifacts if a.kind == "transcript"), None)
    summary_artifact = next((a for a in artifacts if a.kind == "summary"), None)
    item_payload = ItemRead.model_validate(item).model_dump()
    media_entries = parse_media_entries(item.media_urls)
    return ItemDetail(
        **item_payload,
        transcript_path=transcript_artifact.path if transcript_artifact else None,
        summary_path=summary_artifact.path if summary_artifact else None,
        artifacts=[ArtifactRead.model_validate(a) for a in artifacts],
        media_links=[MediaLink(**entry) for entry in media_entries],
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


@app.get("/items/{item_id}/transcript/file")
def download_transcript_file(
    item_id: int,
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
) -> FileResponse:
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    artifact = session.exec(
        select(Artifact).where(Artifact.item_id == item_id, Artifact.kind == "transcript")
    ).first()
    if not artifact:
        raise HTTPException(status_code=404, detail="Transcript not available")
    path = Path(artifact.path)
    if not path.exists():
        raise HTTPException(status_code=404, detail="Transcript file missing")
    return FileResponse(path, media_type="text/plain", filename=path.name)


@app.get("/items/{item_id}/summary/file")
def download_summary_file(
    item_id: int,
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
) -> FileResponse:
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    artifact = session.exec(
        select(Artifact).where(Artifact.item_id == item_id, Artifact.kind == "summary")
    ).first()
    if not artifact:
        raise HTTPException(status_code=404, detail="Summary not available")
    path = Path(artifact.path)
    if not path.exists():
        raise HTTPException(status_code=404, detail="Summary file missing")
    return FileResponse(path, media_type="text/markdown", filename=path.name or f"{item_id}.md")


@app.post("/items/{item_id}/reset", response_model=ItemDetail)
def reset_item(
    item_id: int,
    delete_artifacts: bool = Query(default=True),
    session: Session = Depends(get_session),
    settings: Settings = Depends(get_settings),
) -> ItemDetail:
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    artifacts = session.exec(select(Artifact).where(Artifact.item_id == item_id)).all()
    if delete_artifacts:
        for artifact in artifacts:
            try:
                Path(artifact.path).unlink(missing_ok=True)
            except OSError:
                logger.warning("Failed to remove artifact file %s", artifact.path)
            session.delete(artifact)
    item.status = ItemStatus.DISCOVERED
    item.error = None
    session.add(item)
    session.commit()
    session.refresh(item)
    return get_item(item_id, session)


def run_transcript_job(item_id: int, settings: Settings) -> None:
    ensure_data_dirs(settings)
    engine = get_engine()
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            return
        try:
            logger.info("Starting transcript job for item %s", item_id)
            media_entries = parse_media_entries(item.media_urls)
            if not media_entries:
                fallback_provider = infer_provider_from_url(item.canvas_url)
                fallback_url = (
                    normalize_provider_url(fallback_provider, item.canvas_url)
                    if fallback_provider
                    else item.canvas_url
                )
                if fallback_url:
                    media_entries.append(
                        {
                            "provider": fallback_provider or (item.provider or "fake"),
                            "url": fallback_url,
                        }
                    )

            grouped_urls: dict[str, list[str]] = defaultdict(list)
            for entry in media_entries:
                provider_name = (entry.get("provider") or "fake").lower()
                url = entry.get("url")
                if not url:
                    continue
                grouped_urls[provider_name].append(url)

            if not grouped_urls:
                grouped_urls[(item.provider or "fake").lower()] = [item.canvas_url] if item.canvas_url else []

            transcript_sections: list[tuple[str, str, str]] = []
            missing_urls: list[str] = []

            for provider_name, urls in grouped_urls.items():
                urls = [u for u in urls if u]
                if not urls:
                    continue
                provider = resolve_provider(item, provider_name)
                transcripts = provider.fetch(item, urls)
                for url in urls:
                    text = transcripts.get(url)
                    if text:
                        transcript_sections.append((provider.name, url, text))
                    else:
                        missing_urls.append(url)

            if not transcript_sections:
                if missing_urls:
                    raise RuntimeError(
                        "No transcripts retrieved for URLs: " + ", ".join(missing_urls)
                    )
                raise RuntimeError("No transcripts could be retrieved")

            transcript_text = format_transcript_bundle(transcript_sections)
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
            logger.info("Transcript job completed for item %s", item_id)
        except Exception as exc:  # pragma: no cover - background logging
            logger.exception("Transcript job failed for item %s", item_id)
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
            logger.info("Starting summary job for item %s", item_id)
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
            logger.info("Summary job completed for item %s", item_id)
        except Exception as exc:  # pragma: no cover - background logging
            logger.exception("Summary job failed for item %s", item_id)
            item.status = ItemStatus.FAILED
            item.error = str(exc)
            session.add(item)
            session.commit()
