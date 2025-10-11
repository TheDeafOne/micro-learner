#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

from playwright.sync_api import sync_playwright

DEFAULT_PROFILE_DIR = Path("edge-profile")  # persists cookies/session across runs
DEFAULT_STATE_FILE = Path("playwright-state.json")


def _playwright_config() -> Tuple[str, Path, bool, Path | None]:
    channel = os.getenv("PLAYWRIGHT_BROWSER_CHANNEL", "chromium").strip()
    profile_dir = Path(os.getenv("PLAYWRIGHT_USER_DATA_DIR", DEFAULT_PROFILE_DIR.as_posix()))
    headless = os.getenv("PLAYWRIGHT_HEADLESS", "false").lower() in {"1", "true", "yes"}
    storage_state_env = os.getenv("PLAYWRIGHT_STORAGE_STATE")
    storage_state = (
        Path(storage_state_env).expanduser().resolve()
        if storage_state_env
        else DEFAULT_STATE_FILE.resolve()
    )
    if storage_state_env is None and not storage_state.exists():
        storage_state = None
    elif storage_state and not storage_state.exists():
        storage_state = None
    return channel, profile_dir, headless, storage_state


@dataclass
class ManagedContext:
    context: Any
    browser: Any | None = None

    def __getattr__(self, item):
        return getattr(self.context, item)

    def close(self) -> None:
        try:
            self.context.close()
        finally:
            if self.browser:
                self.browser.close()


def _launch_context(pw):
    channel, profile_dir, headless, storage_state = _playwright_config()
    launch_args = ["--no-sandbox"]
    if headless:
        launch_args.append("--disable-gpu")

    if storage_state and storage_state.exists():
        browser = pw.chromium.launch(
        user_data_dir="/home/woodbkb2/git/micro-learner/backend/edge-profile",
        headless=False,   # keep headed while debugging
        args=[
            "--profile-directory=Default",  # <-- key part
            "--no-sandbox",
            "--disable-gpu"
        ],
    )
        context = browser.new_context(storage_state=str(storage_state))
        return ManagedContext(context, browser)

    profile_dir.mkdir(parents=True, exist_ok=True)
    kwargs = {
        "user_data_dir": str(profile_dir),
        "headless": headless,
        "args": launch_args,
    }
    if channel:
        kwargs["channel"] = channel
    try:
        return ManagedContext(pw.chromium.launch_persistent_context(**kwargs))
    except Exception:
        if channel and channel.lower() != "chromium":
            kwargs.pop("channel", None)
            return ManagedContext(pw.chromium.launch_persistent_context(**kwargs))
        raise


def get_transcript_text(url):
    with sync_playwright() as pw:
        ctx = _launch_context(pw)
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
        ctx = _launch_context(pw)
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
