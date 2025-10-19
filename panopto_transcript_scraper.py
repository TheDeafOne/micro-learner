#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Union
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from bs4 import BeautifulSoup
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, sync_playwright

PROFILE_DIR = Path("edge-profile")  # persists cookies/session across runs
PANOPTO_URL_RE = re.compile(r"panopto\.com/.+(Viewer|Embed)\.aspx.*", re.I)
MS_SSO_RE = re.compile(r"(microsoftonline\.com|/adfs/|/sts/)", re.I)
GOTO_TIMEOUT_MS = 60_000
SSO_TIMEOUT_MS = 300_000
CAPTIONS_TIMEOUT_MS = 20_000


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
    """Parse captions from the HTML DOM without relying on visibility."""
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


def _ensure_panopto_page(page, ctx):
    if PANOPTO_URL_RE.search(page.url):
        return page
    if MS_SSO_RE.search(page.url):
        print("Complete Microsoft SSO in the opened window; waiting…")
        try:
            page.wait_for_url(PANOPTO_URL_RE, timeout=SSO_TIMEOUT_MS)
            return page
        except PlaywrightTimeoutError as exc:
            for candidate in ctx.pages:
                if PANOPTO_URL_RE.search(candidate.url):
                    return candidate
            raise RuntimeError("Timed out waiting for Panopto viewer after SSO.") from exc
    raise RuntimeError(f"Did not reach a Panopto viewer page (current URL: {page.url}).")


def _goto_panopto(page, ctx, url: str):
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=GOTO_TIMEOUT_MS)
    except PlaywrightTimeoutError as exc:
        raise RuntimeError(f"Timed out loading Panopto page: {url}") from exc
    return _ensure_panopto_page(page, ctx)


def _wait_for_captions(page) -> str:
    try:
        page.wait_for_selector('ul.event-tab-list[aria-label="Captions"]', timeout=CAPTIONS_TIMEOUT_MS)
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
        print("Usage: uv run panopto_transcript_scraper.py <panopto_url> [more_urls...]")
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
