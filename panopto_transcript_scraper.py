#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from typing import Dict, List, Union
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

from backend.playwright_utils import launch_context


PANOPTO_URL_RE = re.compile(r"panopto\.com/.+(Viewer|Embed)\.aspx.*", re.I)
MS_SSO_RE = re.compile(r"(microsoftonline\.com|/adfs/|/sts/)", re.I)


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


def get_transcript_text(url: str) -> str | None:
    url = normalize_panopto_url(url)
    print(f"Opening: {url}")
    with sync_playwright() as pw:
        ctx = launch_context(pw)
        try:
            page = ctx.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=10000)
            page = _ensure_panopto_page(page, ctx)
            try:
                page.wait_for_selector('ul.event-tab-list[aria-label="Captions"]', timeout=10000)
            except Exception:
                page.wait_for_load_state("networkidle", timeout=10000)
            html = page.content()
            return _extract_captions_from_html(html)
        finally:
            ctx.close()


def get_transcripts(urls: Union[str, List[str]]) -> Dict[str, str | None]:
    if isinstance(urls, str):
        urls = [urls]

    normalized_urls = [normalize_panopto_url(url) for url in urls]
    results: Dict[str, str | None] = {}
    with sync_playwright() as pw:
        ctx = launch_context(pw)
        try:
            page = ctx.new_page()
            for url in normalized_urls:
                try:
                    print(f"Opening: {url}")
                    page.goto(url, wait_until="domcontentloaded", timeout=10000)
                    page = _ensure_panopto_page(page, ctx)
                    try:
                        page.wait_for_selector('ul.event-tab-list[aria-label="Captions"]', timeout=10000)
                    except Exception:
                        page.wait_for_load_state("networkidle", timeout=10000)
                    html = page.content()
                    results[url] = _extract_captions_from_html(html)
                except Exception:
                    results[url] = None
        finally:
            ctx.close()
    return results


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


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: uv run panopto_transcript_scraper.py <panopto_url> [more_urls...]")
        raise SystemExit(2)

    urls = [normalize_panopto_url(u) for u in sys.argv[1:]]
    if len(urls) == 1:
        print(get_transcript_text(urls[0]) or "")
    else:
        results = get_transcripts(urls)
        for link, text in results.items():
            print("=" * 80)
            print(link)
            print("-" * 80)
            print(text or "(no transcript)")


if __name__ == "__main__":
    main()
