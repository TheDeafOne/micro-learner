from __future__ import annotations

from typing import Any, Optional

import httpx

from .settings import Settings


class CanvasClient:
    def __init__(self, settings: Settings):
        self.base_url = settings.canvas_base_url.rstrip("/")
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Bearer {settings.canvas_token}"},
            timeout=httpx.Timeout(30.0),
        )

    async def __aenter__(self) -> "CanvasClient":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self._client.aclose()

    async def fetch_courses(self) -> list[dict[str, Any]]:
        return await self._paginate("/api/v1/courses?per_page=100")

    async def fetch_modules(self, course_id: int) -> list[dict[str, Any]]:
        return await self._paginate(f"/api/v1/courses/{course_id}/modules?per_page=100")

    async def fetch_module_items(self, course_id: int, module_id: int) -> list[dict[str, Any]]:
        return await self._paginate(
            f"/api/v1/courses/{course_id}/modules/{module_id}/items?per_page=100"
        )

    async def fetch_page_body(self, course_id: int, page_url: str) -> str:
        response = await self._client.get(f"/api/v1/courses/{course_id}/pages/{page_url}")
        response.raise_for_status()
        data = response.json()
        body = data.get("body") or ""
        return body

    async def _paginate(self, path: str) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        next_url: Optional[str] = path
        while next_url:
            response = await self._client.get(next_url)
            response.raise_for_status()
            payload = response.json()
            if isinstance(payload, list):
                results.extend(payload)
            else:
                results.append(payload)
            next_url = self._next_link(response.headers.get("link"))
        return results

    def _next_link(self, link_header: Optional[str]) -> Optional[str]:
        if not link_header:
            return None
        segments = [segment.strip() for segment in link_header.split(",")]
        for segment in segments:
            if ';' not in segment:
                continue
            url_part, *rest = segment.split(";", maxsplit=1)
            rel = rest[0] if rest else ""
            if 'rel="next"' not in rel:
                continue
            url = url_part.strip()
            if url.startswith("<") and url.endswith(">"):
                url = url[1:-1]
            if url.startswith(self.base_url):
                url = url[len(self.base_url):]
            return url
        return None
