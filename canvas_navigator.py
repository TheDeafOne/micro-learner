# ai_lecture_links.py
import asyncio
import os
import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

import llm
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


def extract_links(html):
    soup = BeautifulSoup(html, "html.parser")
    return [a["href"] for a in soup.select("a[href]")]


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

    transcripts_dict = await asyncio.to_thread(zts.get_transcripts, links)
    transcripts = list(transcripts_dict.values())

    summarize_prompt = """
        Summarize this transcript. Describe only the details, don't reference to the speaker or talk in at a higher level.
        Just provide the summarized information in a concise format. Response in markdown. Here is the transcript:
        {transcript_text}
    """
    summary_prompts = [summarize_prompt.format(transcript_text=t) for t in transcripts]
    responses = await multi_query(summary_prompts)

    notes_dir = "lecture-notes"
    out_path = f"{notes_dir}/Module {n}.md".replace(" ", "_")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write("\n\n".join(map(str, responses)))


if __name__ == "__main__":
    asyncio.run(main())
