# Canvas Summarization Backend

FastAPI + SQLite backend that syncs Canvas course structure and produces local transcript and summary files for module items. Zoom and Panopto videos are transcribed via Playwright-driven scrapers so you can reuse the browser automation workflow from the CLI scripts. A mock provider is still available for other sources.

## Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or another PEP 517 compatible installer
- Canvas Personal Access Token with permission to read your courses and modules
- Microsoft Edge (Chromium) with a profile that can access your Panopto/Zoom content
- Playwright browsers installed (`uv run playwright install` once after syncing)

## Installation

```bash
uv sync
```

This installs dependencies defined in `pyproject.toml` into the local virtualenv created by `uv`. After syncing, install Playwright browser binaries:

```bash
uv run playwright install
```

## Configuration

Copy the environment example and fill in your Canvas details:

```bash
cp backend/.env.example .env
```

Set the following variables in `.env`:

- `CANVAS_BASE_URL` – base URL for your Canvas instance (e.g. `https://canvas.instructure.com`)
- `CANVAS_TOKEN` – personal access token
- `OPENAI_API_KEY` – optional; leave blank to use the mock summarizer
- `DATA_DIR` – where transcript/summary files are written (default `./data`)
- `DATABASE_URL` – SQLite connection string (default `sqlite:///./backend.db`)
- `PLAYWRIGHT_BROWSER_CHANNEL` – browser channel for Playwright (`chromium`, `msedge`, etc.)
- `PLAYWRIGHT_USER_DATA_DIR` – path to reuse browser profile (default `edge-profile`)
- `PLAYWRIGHT_HEADLESS` – `true` to run Playwright headless, otherwise `false`

The app auto-creates database tables and ensures transcript/summary directories exist under `DATA_DIR`.

## Running the API

Use `uv` to run the FastAPI app with live reload:

```bash
uv run backend/main.py
```

The server starts on `http://127.0.0.1:8000`. You can also use standard uvicorn syntax:

```bash
uv run uvicorn backend.main:app --reload
```

## API Workflow

1. **Health check** – `GET /health`
2. **Sync courses** – `POST /me/courses/refresh`  
   Populates the `course` table from Canvas.
3. **List courses** – `GET /me/courses`
4. **Sync modules + items** – `POST /courses/{course_id}/modules/refresh`  
   Fetches modules and their items, inferring providers from URLs.
5. **Browse data** – `GET /courses/{id}`, `GET /courses/{id}/modules`, `GET /modules/{id}/items`
6. **Fetch transcript** – `POST /items/{id}/fetch-transcript`  
   Queues a background job that launches the appropriate provider:
   - Panopto → `panopto_transcript_scraper.get_transcripts`
   - Zoom → `zoom_transcript_scraper.get_transcripts`
   - Other → fake provider that returns placeholder text

   The job writes `data/transcripts/{item_id}.txt`, stores/updates an artifact record, and moves the item status to `TRANSCRIPT_READY`.
   For Canvas Pages, the task fetches the page body, extracts every Panopto/Zoom link (mirroring `extract_links` from `canvas_navigator.py`), transcribes them all, and concatenates the transcripts into a single artifact.
7. **Summarize** – `POST /items/{id}/summarize`  
   Requires an existing transcript. Writes `data/summaries/{item_id}.md`, creates/updates the summary artifact, and sets status to `SUMMARY_READY`.
8. **Inspect status** – `GET /items/{id}`  
   Returns item metadata, detected media links, and paths to the generated artifacts.

Background tasks run inside the FastAPI process using `BackgroundTasks`, so the responses return immediately while work continues asynchronously.

## Data Layout

- SQLite database: `backend.db` (configurable via `DATABASE_URL`)
- Transcripts: `data/transcripts/{item_id}.txt`
- Summaries: `data/summaries/{item_id}.md`
- Edge profile directory reused by Playwright: `edge-profile/` (created automatically when scrapers run)

## Development Notes

- `python3 -m compileall backend` ensures syntax validity.
- The Panopto and Zoom providers reuse the CLI scrapers (`panopto_transcript_scraper.py`, `zoom_transcript_scraper.py`) so any improvements there automatically flow into the API.
- The API docs are available at `http://127.0.0.1:8000/docs`.
