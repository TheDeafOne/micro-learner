#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Union
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

PROFILE_DIR = Path("edge-profile")  # persists cookies/session across runs


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
        ctx = pw.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            channel="msedge",
            headless=False,
        )
        try:
            page = ctx.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=6000)

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
                page.wait_for_load_state("networkidle", timeout=6000)

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
        ctx = pw.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            channel="msedge",
            headless=False,
        )
        try:
            page = ctx.new_page()
            for url in urls:
                try:
                    print(f"Opening: {url}")
                    page.goto(url, wait_until="domcontentloaded", timeout=6000)

                    # Wait out Microsoft SSO if it appears
                    page = _ensure_panopto_page(page, ctx)

                    # Captions are present in the initial HTML, but may be injected a bit late
                    try:
                        page.wait_for_selector(
                            'ul.event-tab-list[aria-label="Captions"]', timeout=5000
                        )
                    except Exception:
                        page.wait_for_load_state("networkidle", timeout=6000)

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
