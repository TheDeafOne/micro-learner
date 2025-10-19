import asyncio
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import parse_qs, urlencode, urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from llm import fetch_response
import panopto_transcript_scraper as pts
import zoom_transcript_scraper as zts

load_dotenv()

BASE = os.getenv("CANVAS_BASE_URL", "").rstrip("/")
TOKEN = os.getenv("CANVAS_TOKEN", "")
if not BASE or not TOKEN:
    sys.exit("Set CANVAS_BASE_URL and CANVAS_TOKEN in your environment/.env")

HEADERS = {"Authorization": f"Bearer {TOKEN}"}
DATA_ROOT = Path("data/courses")


def _slugify(value: str, fallback: str) -> str:
    normalized = (
        unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
        if value
        else ""
    )
    normalized = normalized.strip() or fallback
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower())
    return slug.strip("-") or fallback


def get_all(url: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    next_url, query = url, params
    while next_url:
        resp = requests.get(next_url, headers=HEADERS, params=query, timeout=30)
        resp.raise_for_status()
        out.extend(resp.json())
        next_link = None
        if "link" in resp.headers:
            for part in resp.headers["link"].split(","):
                if 'rel="next"' in part:
                    next_link = part[part.find("<") + 1 : part.find(">")]
                    break
        next_url, query = (next_link, None) if next_link else (None, None)
    return out


def list_courses() -> List[Dict[str, Any]]:
    return get_all(urljoin(BASE, "/api/v1/courses"), params={"per_page": 200})


def list_modules(course_id: int) -> List[Dict[str, Any]]:
    return get_all(
        urljoin(BASE, f"/api/v1/courses/{course_id}/modules"),
        params={"per_page": 200},
    )


def list_module_items(course_id: int, module_id: int) -> List[Dict[str, Any]]:
    return get_all(
        urljoin(BASE, f"/api/v1/courses/{course_id}/modules/{module_id}/items"),
        params={"per_page": 200},
    )


def get_page_body(course_id: int, page_url: str) -> str:
    resp = requests.get(
        urljoin(BASE, f"/api/v1/courses/{course_id}/pages/{page_url}"), headers=HEADERS
    )
    resp.raise_for_status()
    return resp.json().get("body", "")


def _to_panopto_viewer(url: str) -> str:
    try:
        parsed = urlparse(url)
        if "panopto.com" not in parsed.netloc.lower():
            return url
        pid = (parse_qs(parsed.query).get("id") or [None])[0]
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
    except Exception:
        return url


def _dedupe_preserve_order(urls: Iterable[str]) -> List[str]:
    seen: Dict[str, None] = {}
    for url in urls:
        if url not in seen:
            seen[url] = None
    return list(seen.keys())


def extract_links(html: str) -> List[str]:
    soup = BeautifulSoup(html, "html.parser")
    candidates: List[str] = []

    for anchor in soup.select("a[href]"):
        href = (anchor.get("href") or "").strip()
        if not href:
            continue
        if href.startswith("/"):
            href = urljoin(BASE, href)
        candidates.append(href)

    for meta in soup.find_all("meta", attrs={"property": "og:url"}):
        content = (meta.get("content") or "").strip()
        if content:
            candidates.append(content)

    for iframe in soup.select("iframe[src]"):
        src = (iframe.get("src") or "").strip()
        if src:
            candidates.append(src)

    normalized: List[str] = []
    for url in candidates:
        if "panopto.com" in url.lower():
            normalized.append(_to_panopto_viewer(url))
        else:
            normalized.append(url)

    return _dedupe_preserve_order(normalized)


def categorize_links(links: Sequence[str]) -> Tuple[List[str], List[str]]:
    zoom = [link for link in links if "zoom.us" in link.lower()]
    panopto = [link for link in links if "panopto.com" in link.lower()]
    return zoom, panopto


async def fetch_transcripts_ordered(
    ordered_links: Sequence[str],
    zoom_links: Sequence[str],
    panopto_links: Sequence[str],
) -> List[Tuple[str, Optional[str]]]:
    zoom_results: Dict[str, Optional[str]] = {}
    panopto_results: Dict[str, Optional[str]] = {}

    if zoom_links:
        zoom_results = await asyncio.to_thread(zts.get_transcripts, list(zoom_links))
    if panopto_links:
        panopto_results = await asyncio.to_thread(
            pts.get_transcripts, list(panopto_links)
        )

    ordered: List[Tuple[str, Optional[str]]] = []
    for link in ordered_links:
        if link in zoom_results:
            ordered.append((link, zoom_results.get(link)))
        elif link in panopto_results:
            ordered.append((link, panopto_results.get(link)))
        else:
            ordered.append((link, None))
    return ordered


async def summarize_transcripts(transcripts: Sequence[str]) -> List[str]:
    if not transcripts:
        return []
    prompt_template = (
        "Summarize this lecture transcript. Focus on the detailed content; avoid "
        "referencing the speaker or meta commentary. Return concise markdown only.\n\n{transcript}"
    )
    prompts = [prompt_template.format(transcript=t) for t in transcripts]
    responses = await asyncio.gather(*(fetch_response(prompt) for prompt in prompts))
    # fetch_response returns (prompt, response_text)
    return [response for _, response in responses]


def prompt_choice(
    options: Sequence[Any],
    label: str,
    formatter: Callable[[Any, int], str],
) -> Any:
    if not options:
        raise ValueError(f"No {label} options available.")

    while True:
        print(f"\nAvailable {label}:")
        for idx, option in enumerate(options, start=1):
            print(f"  [{idx}] {formatter(option, idx)}")
        choice = input(f"Select a {label} by number (or 'q' to quit): ").strip()
        if choice.lower() in {"q", "quit", "exit"}:
            raise SystemExit(0)
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(options):
                return options[idx - 1]
        print(f"Invalid selection '{choice}'. Please try again.")


def ensure_output_paths(
    course_name: str,
    module_name: str,
    item_name: str,
) -> Tuple[Path, Path]:
    course_slug = _slugify(course_name, "course")
    module_slug = _slugify(module_name, "module")
    item_slug = _slugify(item_name, "item")

    base_dir = DATA_ROOT / course_slug / module_slug
    base_dir.mkdir(parents=True, exist_ok=True)

    transcript_path = base_dir / f"transcript_{course_slug}_{module_slug}_{item_slug}.md"
    summary_path = base_dir / f"summary_{course_slug}_{module_slug}_{item_slug}.md"
    return transcript_path, summary_path


def write_transcript_file(
    path: Path,
    course_name: str,
    module_name: str,
    item_name: str,
    transcripts: Sequence[Tuple[str, Optional[str]]],
) -> None:
    sections: List[str] = [
        f"# Transcript for {course_name} – {module_name} – {item_name}",
    ]
    if not transcripts:
        sections.append("_No transcript entries were fetched._")
    else:
        for link, text in transcripts:
            sections.append(f"## {link}\n\n{text if text else '(No transcript found.)'}")
    path.write_text("\n\n".join(sections), encoding="utf-8", newline="")


def write_summary_file(
    path: Path,
    course_name: str,
    module_name: str,
    item_name: str,
    summaries: Sequence[Tuple[str, str]],
) -> None:
    sections: List[str] = [
        f"# Summary for {course_name} – {module_name} – {item_name}",
    ]
    if not summaries:
        sections.append("_No summaries were generated._")
    else:
        for link, summary in summaries:
            sections.append(f"## {link}\n\n{summary}")
    path.write_text("\n\n".join(sections), encoding="utf-8", newline="")


async def process_item(
    course: Dict[str, Any],
    module: Dict[str, Any],
    item: Dict[str, Any],
) -> None:
    course_name = course.get("name") or course.get("course_code") or f"Course {course['id']}"
    module_name = module.get("name") or f"Module {module['id']}"
    item_name = item.get("title") or item.get("page_url") or f"Item {item['id']}"

    print(f"\nFetching page body for '{item_name}'...")
    body = get_page_body(course["id"], item["page_url"])
    if not body:
        print("The selected page is empty. Nothing to process.")
        return

    links = extract_links(body)
    if not links:
        print("No media links were detected on this page.")
        return

    zoom_links, panopto_links = categorize_links(links)
    if not (zoom_links or panopto_links):
        print("Found links, but none are recognized Zoom or Panopto recordings.")
        return

    print(f"Found {len(zoom_links)} Zoom link(s) and {len(panopto_links)} Panopto link(s).")
    media_links = [link for link in links if link in zoom_links or link in panopto_links]
    transcripts_ordered = await fetch_transcripts_ordered(
        media_links, zoom_links, panopto_links
    )

    transcript_path, summary_path = ensure_output_paths(
        course_name, module_name, item_name
    )
    write_transcript_file(transcript_path, course_name, module_name, item_name, transcripts_ordered)
    print(f"Saved transcripts to {transcript_path}")

    valid_transcripts = [(link, text) for link, text in transcripts_ordered if text]
    if not valid_transcripts:
        print("No transcript text was retrieved; skipping summaries.")
        return

    summaries = await summarize_transcripts([text for _, text in valid_transcripts])
    summary_pairs = list(zip([link for link, _ in valid_transcripts], summaries))
    write_summary_file(summary_path, course_name, module_name, item_name, summary_pairs)
    print(f"Saved summaries to {summary_path}")


def main() -> None:
    try:
        print("Loading Canvas courses...")
        courses = list_courses()
        if not courses:
            print("No courses found for the provided Canvas credentials.")
            return

        course = prompt_choice(
            courses,
            label="course",
            formatter=lambda c, _: f"{c.get('name') or c.get('course_code') or c['id']} (id: {c['id']})",
        )

        modules = list_modules(course["id"])
        if not modules:
            print("No modules available in this course.")
            return

        module = prompt_choice(
            modules,
            label="module",
            formatter=lambda m, _: f"{m.get('name', '(no name)')} (id: {m['id']})",
        )

        items = list_module_items(course["id"], module["id"])
        page_items = [item for item in items if item.get("type") == "Page"]
        if not page_items:
            print("No Canvas Page items found in this module; nothing to process.")
            return

        item = prompt_choice(
            page_items,
            label="module item",
            formatter=lambda i, _: f"{i.get('title', '(no title)')} (id: {i['id']})",
        )

        asyncio.run(process_item(course, module, item))
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")


if __name__ == "__main__":
    main()
