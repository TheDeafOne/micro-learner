#!/usr/bin/env python3
from __future__ import annotations

import sys
from typing import Dict, List, Union

from playwright.sync_api import sync_playwright

from backend.playwright_utils import launch_context


def get_transcript_text(url: str) -> str | None:
    with sync_playwright() as pw:
        ctx = launch_context(pw)
        try:
            page = ctx.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=60_000)
            page.wait_for_selector(
                ".transcript-container, .audio-transcript.single-panel",
                timeout=45_000,
            )
            locator = page.locator(
                ".transcript-container, .audio-transcript.single-panel"
            ).first
            return locator.inner_text()
        except Exception:
            return None
        finally:
            ctx.close()


def get_transcripts(urls: Union[str, List[str]]) -> Dict[str, str | None]:
    if isinstance(urls, str):
        urls = [urls]

    results: Dict[str, str | None] = {}
    with sync_playwright() as pw:
        ctx = launch_context(pw)
        try:
            for url in urls:
                text = None
                page = ctx.new_page()
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=60_000)
                    page.wait_for_selector(
                        ".transcript-container, .audio-transcript.single-panel",
                        timeout=45_000,
                    )
                    locator = page.locator(
                        ".transcript-container, .audio-transcript.single-panel"
                    ).first
                    text = locator.inner_text()
                except Exception:
                    text = None
                finally:
                    results[url] = text
                    page.close()
        finally:
            ctx.close()
    return results


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: uv run zoom_transcript_scraper.py <zoom_play_url>")
        raise SystemExit(2)

    url = sys.argv[1]
    print(get_transcript_text(url) or "")


if __name__ == "__main__":
    main()
