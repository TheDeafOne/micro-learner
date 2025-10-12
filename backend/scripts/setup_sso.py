#!/usr/bin/env python3
"""Interactive helper to capture Playwright SSO cookies.

Usage:
    uv run scripts/setup_sso.py --url <login_url>

The script launches a non-headless browser using your PLAYWRIGHT_* settings,
lets you complete Microsoft/Zoom SSO manually, then saves the storage state to
``PLAYWRIGHT_STORAGE_STATE`` (default ``./playwright-state.json``).
"""
from __future__ import annotations

import argparse
from pathlib import Path

from playwright.sync_api import sync_playwright

from playwright_utils import launch_context, load_config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Capture authenticated Playwright storage state.")
    parser.add_argument(
        "--url",
        dest="url",
        default='https://login.microsoftonline.com/',
        help="Optional URL to open automatically (e.g., a Panopto or Canvas page).",
    )
    parser.add_argument(
        "--stay-open",
        dest="stay_open",
        action="store_true",
        help="Keep the browser open after saving state for additional manual verification.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config()
    state_path: Path = config.storage_state_path
    state_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Target storage state: {state_path}")
    print("Launching non-headless browser for manual SSO...")

    with sync_playwright() as pw:
        ctx = launch_context(pw, headless_override=False, use_storage_state=False)
        try:
            if args.url:
                page = ctx.new_page()
                page.goto(args.url, wait_until="load")
            input("Complete SSO in the browser window, then press Enter here to save state...")
            ctx.storage_state(path=str(state_path))
            print(f"✅ Storage state saved to {state_path}")
            if args.stay_open:
                input("Browser will remain open. Press Enter to close...")
        finally:
            ctx.close()


if __name__ == "__main__":
    main()
