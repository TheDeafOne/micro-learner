# Canvas Summarization Backend

FastAPI + SQLite backend that syncs Canvas course structure and produces local transcript and summary files for module items. The service uses fake providers by default so you can run the workflow end-to-end without external dependencies.

## Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or another PEP 517 compatible installer
- Canvas Personal Access Token with permission to read your courses and modules

## Installation

```bash
uv sync
```

This installs dependencies defined in `pyproject.toml` into the local virtualenv created by `uv`.

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
   Queues a background job that writes `data/transcripts/{item_id}.txt`, stores/updates an artifact record, and moves the item status to `TRANSCRIPT_READY`.
7. **Summarize** – `POST /items/{id}/summarize`  
   Requires an existing transcript. Writes `data/summaries/{item_id}.md`, creates/updates the summary artifact, and sets status to `SUMMARY_READY`.
8. **Inspect status** – `GET /items/{id}`  
   Returns item metadata plus paths to the generated artifacts.

Background tasks run inside the FastAPI process using `BackgroundTasks`, so the responses return immediately while work continues asynchronously.

## Data Layout

- SQLite database: `backend.db` (configurable via `DATABASE_URL`)
- Transcripts: `data/transcripts/{item_id}.txt`
- Summaries: `data/summaries/{item_id}.md`

## Development Notes

- `python3 -m compileall backend` ensures syntax validity.
- Add real transcript providers or OpenAI summarization by implementing the stubs in `backend/providers.py` and `backend/summarizer.py`.
- The API docs are available at `http://127.0.0.1:8000/docs`.
