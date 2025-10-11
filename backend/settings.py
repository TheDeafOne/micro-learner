# backend/settings.py
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from dotenv import dotenv_values, find_dotenv
from pydantic import BaseModel, Field


class Settings(BaseModel):
    canvas_base_url: str = Field(..., alias="CANVAS_BASE_URL")
    canvas_token: str = Field(..., alias="CANVAS_TOKEN")
    openai_api_key: Optional[str] = Field(default=None, alias="OPENAI_API_KEY")
    openai_base_url: Optional[str] = Field(default=None, alias="OPENAI_BASE_URL")
    data_dir: Path = Field(default=Path("./data"), alias="DATA_DIR")
    database_url: str = Field(default="sqlite:///./backend.db", alias="DATABASE_URL")

    def model_post_init(self, __context):
        self.data_dir = self.data_dir.resolve()

    def transcripts_dir(self) -> Path:
        return self.data_dir / "transcripts"

    def summaries_dir(self) -> Path:
        return self.data_dir / "summaries"


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
