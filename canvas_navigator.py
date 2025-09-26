# ai_lecture_links.py
import asyncio
import os
import sys
from urllib.parse import parse_qs, urlencode, urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

import llm
import panopto_transcript_scraper as pts
import zoom_transcript_scraper as zts
from llm import multi_query

load_dotenv()

BASE = os.getenv("CANVAS_BASE_URL", "").rstrip("/")
TOKEN = os.getenv("CANVAS_TOKEN", "")
if not BASE or not TOKEN:
    sys.exit("Set CANVAS_BASE_URL and CANVAS_TOKEN in your environment/.env")

HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def get_all(url, params=None):
    out, url = [], url
    while url:
        r = requests.get(url, headers=HEADERS, params=params)
        r.raise_for_status()
        out.extend(r.json())
        # follow pagination via Link header if present
        nxt = None
        if "link" in r.headers:
            for part in r.headers["link"].split(","):
                if 'rel="next"' in part:
                    nxt = part[part.find("<") + 1 : part.find(">")]
        url, params = (nxt, None) if nxt else (None, None)
    return out


def find_ai_course():
    courses = get_all(urljoin(BASE, "/api/v1/courses"), params={"per_page": 100})
    for c in courses:
        name = (c.get("name") or c.get("course_code") or "").lower()
        if "artificial intelligence" in name:
            return c["id"]
    sys.exit("AI course not found in your Canvas list.")


def find_ml_course():
    courses = get_all(urljoin(BASE, "/api/v1/courses"), params={"per_page": 100})
    for c in courses:
        name = (c.get("name") or c.get("course_code") or "").lower()
        if "machine learning" in name:
            return c["id"]
    sys.exit("AI course not found in your Canvas list.")


def find_sma_course():
    courses = get_all(urljoin(BASE, "/api/v1/courses"), params={"per_page": 100})
    for c in courses:
        name = (c.get("name") or c.get("course_code") or "").lower()
        if "social media" in name:
            return c["id"]
    sys.exit("AI course not found in your Canvas list.")


def find_module(course_id, n):
    mods = get_all(
        urljoin(BASE, f"/api/v1/courses/{course_id}/modules"), params={"per_page": 100}
    )
    # Prefer names like "Module N:" or "Module N -"
    want_prefix = f"module {n}".lower()
    for m in mods:
        if m.get("name", "").lower().startswith(want_prefix):
            return m["id"], m["name"]
    sys.exit(
        f"Module {n} not found. Available: "
        + ", ".join(m.get("name", "") for m in mods)
    )


def find_lectures_page(course_id, module_id, n):
    items = get_all(
        urljoin(BASE, f"/api/v1/courses/{course_id}/modules/{module_id}/items"),
        params={"per_page": 100},
    )
    # First try exact "Module N - Lectures", else any Page with "Lectures"
    exact = f"module {n} - lectures"
    page = next(
        (
            i
            for i in items
            if i.get("type") == "Page" and i.get("title", "").lower() == exact
        ),
        None,
    )
    if not page:
        page = next(
            (
                i
                for i in items
                if i.get("type") == "Page" and "lectures" in i.get("title", "").lower()
            ),
            None,
        )
    if not page:
        sys.exit("No 'Lectures' page found in this module.")
    return page["page_url"], page["title"]


def get_page_body(course_id, page_url):
    r = requests.get(
        urljoin(BASE, f"/api/v1/courses/{course_id}/pages/{page_url}"), headers=HEADERS
    )
    r.raise_for_status()
    return r.json().get("body", "")


def _to_panopto_viewer(url: str) -> str:
    try:
        u = urlparse(url)
        if "panopto.com" not in u.netloc.lower():
            return url
        pid = (parse_qs(u.query).get("id") or [None])[0]
        if "Viewer.aspx" in u.path and pid:
            # normalize to clean viewer URL with just ?id=
            return urlunparse(
                (
                    u.scheme,
                    u.netloc,
                    "/Panopto/Pages/Viewer.aspx",
                    "",
                    urlencode({"id": pid}),
                    "",
                )
            )
        if "Embed.aspx" in u.path:
            # convert embed -> viewer (prefer clean ?id= form)
            return urlunparse(
                (
                    u.scheme,
                    u.netloc,
                    "/Panopto/Pages/Viewer.aspx",
                    "",
                    urlencode({"id": pid}) if pid else u.query,
                    "",
                )
            )
        return url
    except Exception:
        return url


def extract_links(html: str):
    soup = BeautifulSoup(html, "html.parser")

    # 1) Normal anchors, if any
    # hrefs = [a.get("href") for a in soup.select("a[href]") if a.get("href")]
    # if hrefs:
    #     # de-dupe, preserve order
    #     return list(dict.fromkeys(hrefs))

    # 2) Fallback to Panopto
    panopto = []

    # 2a) og:url (sometimes present in embedded/preview HTML)
    for m in soup.find_all("meta", attrs={"property": "og:url"}):
        c = m.get("content")
        if c and "panopto.com" in c.lower():
            panopto.append(_to_panopto_viewer(c))

    # 2b) iframe embeds
    for iframe in soup.select("iframe[src]"):
        src = iframe.get("src", "")
        if "panopto.com" in src.lower():
            panopto.append(_to_panopto_viewer(src))

    return list(dict.fromkeys(panopto))


async def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: uv run ai_lecture_links.py <module_number>")
        sys.exit(1)
    n = int(sys.argv[1])

    course_id = find_ai_course()
    module_id, module_name = find_module(course_id, n)
    page_url, page_title = find_lectures_page(course_id, module_id, n)
    body = get_page_body(course_id, page_url)
    links = extract_links(body)

    print(f"\n{module_name} → {page_title}\n")

    if not links:
        print("(No links found in the Lectures page.)")
        return

    print(f"links: {links}")

    zoom_links = [link for link in links if "zoom.us" in link]
    panopto_links = [link for link in links if "panopto.com" in link]
    transcripts = []
    if zoom_links:
        zoom_transcripts_dict = await asyncio.to_thread(zts.get_transcripts, zoom_links)
        transcripts.extend(list(zoom_transcripts_dict.values()))

    if panopto_links:
        panopto_transcripts_dict = await asyncio.to_thread(
            pts.get_transcripts, panopto_links
        )
        transcripts.extend(list(panopto_transcripts_dict.values()))

    notes_dir = "lecture-notes"

    raw_out_path = f"{notes_dir}/raw/{course_id} Module {n} raw.md".replace(" ", "_")
    with open(raw_out_path, "w", encoding="utf-8", newline="") as f:
        f.write("\n\n".join(map(str, transcripts)))
    summarize_prompt = """
        Summarize this transcript. Describe only the details, don't reference to the speaker or talk in at a higher level.
        Just provide the summarized information in a concise format. Response in markdown. Here is the transcript:
        {transcript_text}
    """
    summary_prompts = [summarize_prompt.format(transcript_text=t) for t in transcripts]
    responses = await multi_query(summary_prompts)

    out_path = f"{notes_dir}/{course_id} Module {n}.md".replace(" ", "_")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write("\n\n".join(map(str, responses)))


if __name__ == "__main__":
    asyncio.run(main())
