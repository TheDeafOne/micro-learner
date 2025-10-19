from __future__ import annotations

import asyncio
import logging
from typing import Any

from fastapi import WebSocket


class EventNotifier:
    def __init__(self) -> None:
        self._connections: set[WebSocket] = set()
        self._lock = asyncio.Lock()
        self._loop: asyncio.AbstractEventLoop | None = None
        self._logger = logging.getLogger(__name__)

    def set_loop(self, loop: asyncio.AbstractEventLoop) -> None:
        self._loop = loop

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        async with self._lock:
            self._connections.add(websocket)

    async def disconnect(self, websocket: WebSocket) -> None:
        async with self._lock:
            self._connections.discard(websocket)

    async def _broadcast(self, message: dict[str, Any]) -> None:
        data = message
        dead: list[WebSocket] = []
        async with self._lock:
            connections = list(self._connections)
        for connection in connections:
            try:
                await connection.send_json(data)
            except Exception:
                dead.append(connection)
        if dead:
            async with self._lock:
                for connection in dead:
                    self._connections.discard(connection)

    def publish(self, message: dict[str, Any]) -> None:
        if not self._loop:
            return
        future = asyncio.run_coroutine_threadsafe(self._broadcast(message), self._loop)

        def _handle_result(result: asyncio.Future[Any]) -> None:
            try:
                exc = result.exception()
            except Exception as err:  # pragma: no cover - defensive logging
                self._logger.exception("Unhandled websocket broadcast error", exc_info=err)
                return
            if exc:
                self._logger.exception("Error broadcasting websocket message", exc_info=exc)

        future.add_done_callback(_handle_result)


notifier = EventNotifier()
