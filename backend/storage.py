from __future__ import annotations

from pathlib import Path

from .settings import Settings


def ensure_data_dirs(settings: Settings) -> None:
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    settings.transcripts_dir().mkdir(parents=True, exist_ok=True)
    settings.summaries_dir().mkdir(parents=True, exist_ok=True)


def transcript_path(item_id: int, settings: Settings) -> Path:
    return settings.transcripts_dir() / f"{item_id}.txt"


def summary_path(item_id: int, settings: Settings) -> Path:
    return settings.summaries_dir() / f"{item_id}.md"


def write_transcript(item_id: int, text: str, settings: Settings) -> Path:
    path = transcript_path(item_id, settings)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def write_summary(item_id: int, text: str, settings: Settings) -> Path:
    path = summary_path(item_id, settings)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path
