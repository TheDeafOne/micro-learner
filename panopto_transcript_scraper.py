#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Union
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from bs4 import BeautifulSoup
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

PROFILE_DIR = Path("edge-profile")  # persists cookies/session across runs
PANOPTO_URL_RE = re.compile(r"panopto\.com/.+(Viewer|Embed)\.aspx.*", re.I)
MS_SSO_RE = re.compile(r"(microsoftonline\.com|/adfs/|/sts/)", re.I)
GOTO_TIMEOUT_MS = 60_000
CAPTIONS_TIMEOUT_MS = 60_000


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


def _extract_captions_from_html(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    ul = soup.select_one('ul.event-tab-list[aria-label="Captions"]')
    if not ul:
        return None

    lines: List[str] = []
    for node in ul.select("li.index-event .event-text"):
        text = node.get_text(separator=" ", strip=True)
        if text:
            lines.append(text)
    return "\n".join(lines) if lines else None


def _ensure_panopto_page(page, ctx):
    if MS_SSO_RE.search(page.url):
        try:
            page.wait_for_url(PANOPTO_URL_RE, timeout=300_000)
        except Exception:
            for candidate in ctx.pages:
                if PANOPTO_URL_RE.search(candidate.url):
                    return candidate
    return page


def normalize_panopto_url(url: str) -> str:
    parsed = urlparse(url)
    if "panopto.com" not in parsed.netloc.lower():
        return url
    query = parse_qs(parsed.query)
    pid = (query.get("id") or [None])[0]
    if "Viewer.aspx" in parsed.path and pid:
        return urlunparse(
            (
                parsed.scheme,
                parsed.netloc,
                "/Panopto/Pages/Viewer.aspx",
                "",
                urlencode({"id": pid}),
                "",
            )
        )
    if "Embed.aspx" in parsed.path:
        return urlunparse(
            (
                parsed.scheme,
                parsed.netloc,
                "/Panopto/Pages/Viewer.aspx",
                "",
                urlencode({"id": pid}) if pid else parsed.query,
                "",
            )
        )
    return url


def _ensure_panopto_page(ctx):
    informed_login = False
    while True:
        pages = list(ctx.pages)
        if not pages:
            raise RuntimeError(
                "All browser windows were closed before reaching the Panopto viewer."
            )
        for candidate in pages:
            try:
                url = candidate.url
            except Exception:
                continue
            if not url:
                continue
            if PANOPTO_URL_RE.search(url):
                return candidate
        if not informed_login and any(
            MS_SSO_RE.search(getattr(p, "url", "") or "") for p in pages
        ):
            print("Complete Microsoft SSO in the opened window; waiting…")
            informed_login = True
        try:
            pages[0].wait_for_timeout(1000)
        except Exception:
            pass


# Add this near your constants
CAPTIONS_TAB_SELECTOR = "#transcriptTabHeader, div.event-tab-header[aria-controls='transcriptTabPane'], [role='tab'][aria-controls='transcriptTabPane']"


# Add this helper
def _open_captions_tab(page) -> None:
    """
    Ensure the 'Captions' tab is selected. If the tab exists but isn't selected, click it.
    """
    try:
        # Wait for the captions tab to be present in the DOM
        page.wait_for_selector(CAPTIONS_TAB_SELECTOR, timeout=CAPTIONS_TIMEOUT_MS)
    except PlaywrightTimeoutError as exc:
        raise RuntimeError("Could not find the Panopto 'Captions' tab.") from exc

    header = page.query_selector(CAPTIONS_TAB_SELECTOR)
    if not header:
        raise RuntimeError("The 'Captions' tab header was not found after it appeared.")

    # Click only if not already selected
    aria_selected = header.get_attribute("aria-selected")
    if aria_selected != "true":
        header.click()
        # Tiny pause to allow panel to render
        page.wait_for_timeout(250)


def _goto_panopto(page, ctx, url: str):
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=GOTO_TIMEOUT_MS)
    except PlaywrightTimeoutError as exc:
        raise RuntimeError(f"Timed out loading Panopto page: {url}") from exc
    page.wait_for_timeout(500)
    return _ensure_panopto_page(ctx)


# Replace your existing _wait_for_captions with this version
def _wait_for_captions(page) -> str:
    # NEW: open the Captions tab before waiting for the list
    _open_captions_tab(page)

    try:
        page.wait_for_selector(
            'ul.event-tab-list[aria-label="Captions"]',
            timeout=CAPTIONS_TIMEOUT_MS,
        )
    except PlaywrightTimeoutError as exc:
        raise RuntimeError("Timed out waiting for Panopto captions panel.") from exc

    transcript = _extract_captions_from_html(page.content())
    if not transcript:
        raise RuntimeError("Panopto transcript was empty.")
    return transcript


def get_transcript_text(url: str) -> str:
    url = normalize_panopto_url(url)
    print(f"Opening: {url}")
    with sync_playwright() as pw:
        ctx = _launch_context(pw)
        try:
            page = ctx.new_page()
            try:
                current_page = _goto_panopto(page, ctx, url)
                transcript = _wait_for_captions(current_page)
            finally:
                _close_all_pages(ctx)
        finally:
            ctx.close()
    return transcript


def get_transcripts(urls: Union[str, List[str]]) -> Dict[str, str]:
    if isinstance(urls, str):
        urls = [urls]

    normalized_urls = [normalize_panopto_url(url) for url in urls]
    results: Dict[str, str] = {}
    with sync_playwright() as pw:
        ctx = _launch_context(pw)
        try:
            for url in normalized_urls:
                print(f"Opening: {url}")
                page = ctx.new_page()
                try:
                    current_page = _goto_panopto(page, ctx, url)
                    results[url] = _wait_for_captions(current_page)
                finally:
                    _close_all_pages(ctx)
        finally:
            ctx.close()
    return results


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "Usage: uv run panopto_transcript_scraper.py <panopto_url> [more_urls...]"
        )
        raise SystemExit(2)

    urls = [normalize_panopto_url(u) for u in sys.argv[1:]]
    if len(urls) == 1:
        print(get_transcript_text(urls[0]))
    else:
        results = get_transcripts(urls)
        for link, text in results.items():
            print("=" * 80)
            print(link)
            print("-" * 80)
            print(text)


if __name__ == "__main__":
    main()
