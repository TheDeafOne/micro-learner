from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict
from sqlmodel import Field, SQLModel

from .models import ItemStatus


class CourseRead(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    last_synced_at: Optional[datetime] = None


class ModuleRead(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    course_id: int
    title: str
    position: Optional[int] = None
    last_synced_at: Optional[datetime] = None


class ItemRead(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    module_id: int
    type: Optional[str] = None
    title: str
    canvas_url: Optional[str] = None
    provider: Optional[str] = None
    status: ItemStatus
    error: Optional[str] = None
    last_synced_at: Optional[datetime] = None


class ArtifactRead(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    item_id: int
    kind: str
    path: str
    created_at: datetime


class ItemDetail(ItemRead):
    model_config = ConfigDict(from_attributes=True)

    transcript_path: Optional[str] = None
    summary_path: Optional[str] = None
    artifacts: list[ArtifactRead] = Field(default_factory=list)


class RefreshResult(BaseModel):
    count: int
    detail: str
