# backend/settings.py
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from dotenv import dotenv_values, find_dotenv
from pydantic import BaseModel, Field, model_validator


def _default_cors_origins() -> list[str]:
    return [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]


class Settings(BaseModel):
    canvas_base_url: str = Field(..., alias="CANVAS_BASE_URL")
    canvas_token: str = Field(..., alias="CANVAS_TOKEN")
    openai_api_key: Optional[str] = Field(default=None, alias="OPENAI_API_KEY")
    openai_base_url: Optional[str] = Field(default=None, alias="OPENAI_BASE_URL")
    data_dir: Path = Field(default=Path("./data"), alias="DATA_DIR")
    database_url: str = Field(default="sqlite:///./backend.db", alias="DATABASE_URL")
    playwright_browser_channel: str = Field(
        default="chromium",
        alias="PLAYWRIGHT_BROWSER_CHANNEL",
    )
    playwright_user_data_dir: Path = Field(
        default=Path("edge-profile"),
        alias="PLAYWRIGHT_USER_DATA_DIR",
    )
    playwright_headless: bool = Field(
        default=True,
        alias="PLAYWRIGHT_HEADLESS",
    )
    playwright_storage_state: Optional[Path] = Field(
        default=None,
        alias="PLAYWRIGHT_STORAGE_STATE",
    )
    cors_origins: list[str] = Field(default_factory=_default_cors_origins, alias="CORS_ORIGINS")

    @model_validator(mode="before")
    @classmethod
    def _normalize_cors_origins(cls, data: dict | None) -> dict | None:
        if not data:
            return data
        raw = data.get("CORS_ORIGINS") or data.get("cors_origins")
        if isinstance(raw, str):
            items = [item.strip() for item in raw.split(",") if item.strip()]
            data["cors_origins"] = items
        return data

    def model_post_init(self, __context):
        self.data_dir = self.data_dir.resolve()
        self.playwright_user_data_dir = self.playwright_user_data_dir.resolve()
        if self.playwright_storage_state:
            self.playwright_storage_state = Path(self.playwright_storage_state).resolve()
        self.apply_playwright_env()

    def transcripts_dir(self) -> Path:
        return self.data_dir / "transcripts"

    def summaries_dir(self) -> Path:
        return self.data_dir / "summaries"

    def apply_playwright_env(self) -> None:
        os.environ.setdefault("PLAYWRIGHT_BROWSER_CHANNEL", self.playwright_browser_channel)
        os.environ.setdefault("PLAYWRIGHT_USER_DATA_DIR", str(self.playwright_user_data_dir))
        os.environ.setdefault(
            "PLAYWRIGHT_HEADLESS",
            "true" if self.playwright_headless else "false",
        )
        if self.playwright_storage_state:
            os.environ.setdefault("PLAYWRIGHT_STORAGE_STATE", str(self.playwright_storage_state))


def get_settings() -> Settings:
    # Find a .env by walking up from CWD; fall back to repo root relative to this file.
    env_path = find_dotenv(usecwd=True)
    if not env_path:
        env_path = str(Path(__file__).resolve().parents[1] / ".env")

    # Load key/values from .env WITHOUT mutating process env
    env_from_file = dotenv_values(env_path)

    # Merge: real environment wins over .env (so CI/secrets override)
    merged = {**env_from_file, **os.environ}

    # Validate against aliases like CANVAS_BASE_URL / CANVAS_TOKEN
    return Settings.model_validate(merged)
