#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Union

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, sync_playwright

PROFILE_DIR = Path("edge-profile")  # persists cookies/session across runs
TRANSCRIPT_SELECTOR = ".transcript-container, .audio-transcript.single-panel"
GOTO_TIMEOUT_MS = 60_000
TRANSCRIPT_TIMEOUT_MS = 45_000


def _launch_context(pw):
    return pw.chromium.launch_persistent_context(
        user_data_dir=str(PROFILE_DIR),
        channel="msedge",
        headless=False,
    )


def _goto_zoom(page, url: str) -> None:
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=GOTO_TIMEOUT_MS)
    except PlaywrightTimeoutError as exc:
        raise RuntimeError(f"Timed out loading Zoom page: {url}") from exc


def _wait_for_transcript(page) -> str:
    try:
        page.wait_for_selector(TRANSCRIPT_SELECTOR, timeout=TRANSCRIPT_TIMEOUT_MS)
    except PlaywrightTimeoutError as exc:
        raise RuntimeError("Timed out waiting for Zoom transcript to render.") from exc
    locator = page.locator(TRANSCRIPT_SELECTOR).first
    text = locator.inner_text()
    if not text or not text.strip():
        raise RuntimeError("Zoom transcript was empty.")
    return text


def get_transcript_text(url: str) -> str:
    with sync_playwright() as pw:
        ctx = _launch_context(pw)
        try:
            page = ctx.new_page()
            try:
                _goto_zoom(page, url)
                return _wait_for_transcript(page)
            finally:
                page.close()
        finally:
            ctx.close()


def get_transcripts(urls: Union[str, List[str]]) -> Dict[str, str]:
    """Open each Zoom link in the same Edge profile and grab transcript text."""
    if isinstance(urls, str):
        urls = [urls]

    results: Dict[str, str] = {}
    with sync_playwright() as pw:
        ctx = _launch_context(pw)
        try:
            for url in urls:
                page = ctx.new_page()
                try:
                    _goto_zoom(page, url)
                    results[url] = _wait_for_transcript(page)
                finally:
                    page.close()
        finally:
            ctx.close()
    return results


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: uv run zoom_transcript_scraper.py <zoom_play_url>")
        raise SystemExit(2)

    url = sys.argv[1]
    print(get_transcript_text(url))


if __name__ == "__main__":
    main()
