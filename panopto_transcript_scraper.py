#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
DEFAULT_PROFILE_DIR = Path("/home/woodbkb2/git/micro-learner/backend/edge-profile")  # <-- match the working path
DEFAULT_STATE_FILE = Path("playwright-state.json")  # unused for persistent

def _playwright_config() -> tuple[str|None, Path, bool, Path|None]:
    # no channel needed for persistent
    channel = None
    profile_dir = Path(os.getenv("PLAYWRIGHT_USER_DATA_DIR", DEFAULT_PROFILE_DIR.as_posix()))
    # force headed while debugging (ignore env); flip to True later if needed
    headless = False
    storage_state = None
    return channel, profile_dir, headless, storage_state

def _launch_context(pw):
    """
    Launch the SAME persistent profile you used manually.
    """
    _channel, profile_dir, headless, _ = _playwright_config()

    profile_name = "Default"
    profile_dir.mkdir(parents=True, exist_ok=True)

    launch_args = [
        "--no-sandbox",
        f"--profile-directory={profile_name}",
        "--disable-gpu" if headless else "",
    ]
    launch_args = [a for a in launch_args if a]  # drop blanks

    ctx = pw.chromium.launch_persistent_context(
        user_data_dir=str(profile_dir),   # <-- absolute /backend/edge-profile
        headless=headless,                # <-- headed for now
        args=launch_args,
        # if you’re behind a corp proxy, uncomment and set it:
        # proxy={"server": "http://PROXY_HOST:PROXY_PORT"},
    )
    return ManagedContext(ctx)

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


def _extract_captions_from_html(html: str) -> str | None:
    """Parse captions from the HTML DOM without relying on visibility."""
    soup = BeautifulSoup(html, "html.parser")

    # Panopto captions live under: ul.event-tab-list[aria-label="Captions"] > li.index-event .event-text
    ul = soup.select_one('ul.event-tab-list[aria-label="Captions"]')
    if not ul:
        return None

    lines: List[str] = []
    for node in ul.select("li.index-event .event-text"):
        # join nested spans/divs cleanly
        text = node.get_text(separator=" ", strip=True)
        if text:
            lines.append(text)
    return "\n".join(lines) if lines else None


def get_transcript_text(url: str) -> str | None:
    print(f"Opening: {url}")
    with sync_playwright() as pw:
        ctx = _launch_context(pw)
        try:
            page = ctx.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=10000)

            # If we hit Microsoft/ADFS, wait until we’re back on Panopto (same tab or a new one)
            if re.search(r"(microsoftonline\.com|/adfs/|/sts/)", page.url, re.I):
                print("Complete Microsoft SSO in the opened window; waiting…")
                try:
                    page.wait_for_url(
                        re.compile(r"panopto\.com/.+(Viewer|Embed)\.aspx.*", re.I),
                        timeout=300_000,
                    )
                except:
                    # SSO might have continued in a new tab; pick a Panopto tab if one exists
                    for p in ctx.pages:
                        if re.search(
                            r"panopto\.com/.+(Viewer|Embed)\.aspx", p.url, re.I
                        ):
                            page = p
                            break

            # Wait until captions HTML exists (Panopto injects it after load)
            try:
                page.wait_for_selector(
                    'ul.event-tab-list[aria-label="Captions"]', timeout=50
                )
            except:
                # Give it a little more time if late-injected
                page.wait_for_load_state("networkidle", timeout=10000)

            html = page.content()
            return _extract_captions_from_html(html)
        finally:
            ctx.close()


PANOPTO_URL_RE = re.compile(r"panopto\.com/.+(Viewer|Embed)\.aspx.*", re.I)
MS_SSO_RE = re.compile(r"(microsoftonline\.com|/adfs/|/sts/)", re.I)


def _ensure_panopto_page(page, ctx):
    """If we're on MS SSO, wait until we land back on a Panopto page.
    Also handle the case where SSO continues in a new tab."""
    if MS_SSO_RE.search(page.url):
        print("Complete Microsoft SSO in the opened window; waiting…")
        try:
            page.wait_for_url(PANOPTO_URL_RE, timeout=5000)  # up to 5 minutes
        except Exception:
            # SSO might have finished in a different tab—pick the Panopto tab if present
            for p in ctx.pages:
                if PANOPTO_URL_RE.search(p.url):
                    page = p
                    break
    return page


def get_transcripts(urls: Union[str, List[str]]) -> Dict[str, str | None]:
    """Open each Panopto link in one Edge profile, wait for SSO if needed,
    and return {url: captions_text or None}."""
    if isinstance(urls, str):
        urls = [urls]

    results: Dict[str, str | None] = {}
    with sync_playwright() as pw:
        ctx = _launch_context(pw)
        try:
            page = ctx.new_page()
            for url in urls:
                try:
                    print(f"Opening: {url}")
                    page.goto(url, wait_until="domcontentloaded", timeout=10000)

                    # Wait out Microsoft SSO if it appears
                    page = _ensure_panopto_page(page, ctx)

                    # Captions are present in the initial HTML, but may be injected a bit late
                    try:
                        page.wait_for_selector(
                            'ul.event-tab-list[aria-label="Captions"]', timeout=10000
                        )
                    except Exception:
                        page.wait_for_load_state("networkidle", timeout=10000)

                    html = page.content()
                    results[url] = _extract_captions_from_html(html)
                except Exception:
                    results[url] = None
        finally:
            ctx.close()
    return results


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: uv run panopto_transcripts.py <panopto_url_or_embed> [more_urls...]"
        )
        raise SystemExit(2)

    urls = sys.argv[1:]
    if len(urls) == 1:
        print(get_transcript_text(urls[0]) or "")
    else:
        out = get_transcripts(urls)
        for link, txt in out.items():
            print("=" * 80)
            print(link)
            print("-" * 80)
            print(txt or "(no transcript)")


if __name__ == "__main__":
    main()
