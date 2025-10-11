#!/usr/bin/env python3
"""
One-time Microsoft SSO setup for Playwright.

- If a valid storage state exists (auth/state.json with at least one unexpired
  microsoftonline cookie), print status and exit.
- Otherwise, launch a headed browser, let the user complete SSO manually, then
  save storage state for reuse by headless jobs.

Usage:
  python scripts/setup_sso.py
  python scripts/setup_sso.py --force
  python scripts/setup_sso.py --check-only
  python scripts/setup_sso.py --target-url https://login.microsoftonline.com/

Environment:
  TARGET_URL (optional): override the login URL without CLI flag.
  PLAYWRIGHT_BROWSERS_PATH (optional): if you manage browser install centrally.
"""

from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
from datetime import datetime, timezone, timedelta
import sys

from playwright.sync_api import sync_playwright

# --- Config: match your project layout from the traceback ---
REPO_ROOT = Path(__file__).resolve().parents[1]  # adjust if you move this file
USER_DATA_DIR = REPO_ROOT / "backend" / "edge-profile"
STORAGE_STATE_PATH = REPO_ROOT / "auth" / "state.json"

# A URL that reliably lands you on Microsoft login; you can supply a tenant- or app-specific URL.
DEFAULT_TARGET_URL = os.environ.get("TARGET_URL", "https://login.microsoftonline.com/")

MICROSOFT_COOKIE_HOSTS = (
    ".login.microsoftonline.com",
    "login.microsoftonline.com",
    ".microsoftonline.com",
    "microsoftonline.com",
    ".msauth.net",
    ".msftauth.net",
    ".live.com",
)

MIN_REMAINING = timedelta(hours=4)  # require at least 4h remaining on any cookie


def _now_ts() -> int:
    return int(datetime.now(tz=timezone.utc).timestamp())


def _has_valid_ms_cookies(state: dict) -> bool:
    """
    Heuristic: storage state contains at least one non-expired cookie
    for a microsoft login domain, with >= MIN_REMAINING before expiry.
    Session cookies (no 'expires') are ignored because they won't survive a fresh run.
    """
    cookies = state.get("cookies", [])
    if not cookies:
        return False

    now = _now_ts()
    threshold = now + int(MIN_REMAINING.total_seconds())

    for c in cookies:
        domain = (c.get("domain") or "").lower()
        exp = c.get("expires")  # seconds since epoch (int) or -1 / None for session cookie
        if not domain or exp is None or exp <= 0:
            continue  # skip session cookies or malformed

        if any(domain.endswith(host) for host in MICROSOFT_COOKIE_HOSTS):
            if exp >= threshold:
                return True

    return False


def check_state(path: Path) -> tuple[bool, str]:
    if not path.exists():
        return False, f"No storage state found at {path}"

    try:
        state = json.loads(path.read_text())
    except Exception as e:
        return False, f"Failed to parse storage state ({e})."

    if _has_valid_ms_cookies(state):
        return True, f"Valid Microsoft auth state found at {path}"
    else:
        return False, "Storage state exists but appears expired/invalid for Microsoft SSO."


def ensure_dirs():
    (STORAGE_STATE_PATH.parent).mkdir(parents=True, exist_ok=True)
    USER_DATA_DIR.mkdir(parents=True, exist_ok=True)


def require_display_for_headed():
    if sys.platform.startswith(("linux",)) and not os.environ.get("DISPLAY"):
        # Headed Chromium needs an X server (e.g., xvfb).
        raise RuntimeError(
            "No DISPLAY detected. For the one-time manual login, run under a virtual X server:\n"
            "  xvfb-run -a python scripts/setup_sso.py\n"
            "Or perform this step on a machine with a GUI, then copy auth/state.json to the server."
        )


def do_manual_login(target_url: str):
    print("Launching a headed browser for one-time Microsoft SSO...")
    require_display_for_headed()

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,  # headed so you can complete SSO
            args=["--no-sandbox"],
        )
        try:
            page = ctx.new_page()
            print(f"Opening: {target_url}")
            page.goto(target_url, wait_until="load")
            print(
                "\nComplete the sign-in flow (including MFA if required).\n"
                "When you reach your post-login landing page, return here and press Enter."
            )
            input("Press Enter to save the session... ")
            ensure_dirs()
            ctx.storage_state(path=str(STORAGE_STATE_PATH))
            print(f"Saved storage state to: {STORAGE_STATE_PATH}")
        finally:
            ctx.close()


def verify_headless_can_start() -> bool:
    """Try to start a headless persistent context using the saved profile."""
    try:
        with sync_playwright() as p:
            ctx = p.chromium.launch_persistent_context(
                user_data_dir=str(USER_DATA_DIR),
                headless=True,
                args=["--no-sandbox", "--disable-gpu"],
            )
            ctx.close()
        return True
    except Exception as e:
        print(f"Headless launch smoke test failed: {e}")
        return Fal


def main():
    parser = argparse.ArgumentParser(description="One-time Microsoft SSO setup for Playwright.")
    parser.add_argument("--force", action="store_true", help="Force a fresh manual login and overwrite state.")
    parser.add_argument("--check-only", action="store_true", help="Only check status; do not launch a browser.")
    parser.add_argument("--target-url", default=DEFAULT_TARGET_URL, help="URL to start the login flow.")
    args = parser.parse_args()

    ensure_dirs()

    if args.force:
        do_manual_login(args.target_url)
        ok = verify_headless_can_start()
        if ok:
            print("✅ Headless reuse verified. You’re all set.")
        else:
            print("⚠️ Saved state, but headless launch check failed. You can still try your job.")
        return

    ok, msg = check_state(STORAGE_STATE_PATH)
    print(msg)

    if args.check_only:
        return

    if ok:
        print("✅ SSO already set up. Nothing to do.")
        # Optional: quick headless smoke test.
        verify_headless_can_start()
        return

    # Not OK → guide user through one-time headed login
    do_manual_login(args.target_url)
    ok2, msg2 = check_state(STORAGE_STATE_PATH)
    print(msg2)
    ok_smoke = verify_headless_can_start()

    if ok2 and ok_smoke:
        print("✅ Done. Future scrapes can run headlessly using the saved state.")
    else:
        print("⚠️ Saved state, but validation was inconclusive. Try your pipeline; refresh if needed with --force.")


if __name__ == "__main__":
    main()
