#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
import re
from typing import Dict, List, Union

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, sync_playwright

PROFILE_DIR = Path("edge-profile")  # persists cookies/session across runs
TRANSCRIPT_SELECTOR = ".transcript-container, .audio-transcript.single-panel"
GOTO_TIMEOUT_MS = 60_000
TRANSCRIPT_TIMEOUT_MS = 45_000
MS_SSO_RE = re.compile(r"(microsoftonline\.com|/adfs/|/sts/)", re.I)
ZOOM_RECORDING_RE = re.compile(r"zoom\.(us|com)/.*(rec|recording)", re.I)


def _launch_context(pw):
    return pw.chromium.launch_persistent_context(
        user_data_dir=str(PROFILE_DIR),
        channel="msedge",
        headless=False,
    )


def _close_all_pages(ctx) -> None:
    for page in list(ctx.pages):
        try:
            page.close()
        except Exception:
            pass


def _goto_zoom(page, url: str):
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=GOTO_TIMEOUT_MS)
    except PlaywrightTimeoutError as exc:
        raise RuntimeError(f"Timed out loading Zoom page: {url}") from exc
    return page


def _ensure_zoom_recording(page, ctx):
    if ZOOM_RECORDING_RE.search(page.url):
        return page
    if MS_SSO_RE.search(page.url):
        print("Complete Microsoft login for Zoom in the opened browser window; waiting…")
        while True:
            for candidate in ctx.pages:
                try:
                    url = candidate.url
                except Exception:
                    continue
                if url and ZOOM_RECORDING_RE.search(url):
                    return candidate
            if page.is_closed():
                raise RuntimeError(
                    "The authentication window closed before reaching the Zoom recording."
                )
            page.wait_for_timeout(1000)
            if not page.is_closed() and ZOOM_RECORDING_RE.search(page.url):
                return page
    return page


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
            current_page = page
            try:
                current_page = _ensure_zoom_recording(_goto_zoom(page, url), ctx)
                try:
                    current_url = current_page.url
                except Exception:
                    current_url = ""
                if not current_url or not ZOOM_RECORDING_RE.search(current_url):
                    raise RuntimeError(
                        "Did not reach a Zoom recording page after login. "
                        "Ensure the recording loads in the opened browser window."
                    )
                return _wait_for_transcript(current_page)
            finally:
                _close_all_pages(ctx)
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
                current_page = page
                try:
                    current_page = _ensure_zoom_recording(_goto_zoom(page, url), ctx)
                    try:
                        current_url = current_page.url
                    except Exception:
                        current_url = ""
                    if not current_url or not ZOOM_RECORDING_RE.search(current_url):
                        raise RuntimeError(
                            "Did not reach a Zoom recording page after login. "
                            "Ensure the recording loads in the opened browser window."
                        )
                    results[url] = _wait_for_transcript(current_page)
                finally:
                    _close_all_pages(ctx)
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
