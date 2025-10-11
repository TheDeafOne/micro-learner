from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel


class ItemStatus(str, Enum):
    DISCOVERED = "DISCOVERED"
    TRANSCRIPT_READY = "TRANSCRIPT_READY"
    SUMMARY_READY = "SUMMARY_READY"
    FAILED = "FAILED"


class Course(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str
    last_synced_at: Optional[datetime] = None


class Module(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    course_id: int = Field(foreign_key="course.id", index=True)
    title: str
    position: Optional[int] = None
    last_synced_at: Optional[datetime] = None


class Item(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    module_id: int = Field(foreign_key="module.id", index=True)
    type: Optional[str] = None
    title: str
    canvas_url: Optional[str] = None
    provider: Optional[str] = None
    status: ItemStatus = Field(default=ItemStatus.DISCOVERED)
    error: Optional[str] = None
    last_synced_at: Optional[datetime] = None


class Artifact(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("item_id", "kind", name="uix_item_kind"),)

    id: Optional[int] = Field(primary_key=True)
    item_id: int = Field(foreign_key="item.id", index=True)
    kind: str = Field(index=True)
    path: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
