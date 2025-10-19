#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Union

from playwright.sync_api import sync_playwright

PROFILE_DIR = Path("edge-profile")  # persists cookies/session across runs


def get_transcript_text(url):
    with sync_playwright() as pw:
        # Use installed Edge, headed (no headless.exe); avoids the firewall block
        ctx = pw.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            channel="msedge",
            headless=False,
        )
        page = ctx.new_page()
        page.goto(url, wait_until="domcontentloaded")
        text = page.locator(".transcript-container").inner_text()
        ctx.close()
    return text


def get_transcripts(urls: Union[str, List[str]]) -> Dict[str, str]:
    """Open each Zoom link in the same Edge profile and grab transcript text.
    Returns {url: transcript_text or None}."""
    if isinstance(urls, str):
        urls = [urls]

    results: Dict[str, str] = {}
    with sync_playwright() as pw:
        ctx = pw.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),  # existing profile with your SSO
            channel="msedge",
            headless=False,
        )
        try:
            for url in urls:
                text = None
                page = ctx.new_page()
                try:
                    page.goto(url, wait_until="domcontentloaded",
                              timeout=60_000)
                    # Wait for transcript to render; support either container class you’ve seen
                    page.wait_for_selector(
                        ".transcript-container, .audio-transcript.single-panel",
                        timeout=45_000
                    )
                    text = page.locator(
                        ".transcript-container, .audio-transcript.single-panel"
                    ).first.inner_text()
                except Exception:
                    text = None
                finally:
                    results[url] = text
                    page.close()
        finally:
            ctx.close()
    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run open_zoom_min.py \"<zoom_play_url>\"")
        raise SystemExit(2)

    url = sys.argv[1]

    print(get_transcript_text(url))


if __name__ == "__main__":
    main()
