from __future__ import annotations

from functools import lru_cache
from typing import Generator

from sqlmodel import Session, SQLModel, create_engine

from .settings import get_settings


@lru_cache(maxsize=1)
def get_engine():
    settings = get_settings()
    connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
    return create_engine(settings.database_url, connect_args=connect_args)


def get_session() -> Generator[Session, None, None]:
    with Session(get_engine()) as session:
        yield session


def init_db() -> None:
    SQLModel.metadata.create_all(get_engine())
