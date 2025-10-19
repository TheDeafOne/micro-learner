# Codex Prompt: Backend MVP Plan

Build a **FastAPI + SQLite** backend for a Canvas summarization tool MVP.  
Goal: list courses/modules/items from Canvas, trigger transcript + summary jobs, store outputs locally.  
No Redis, no SSE, no OAuth — minimal infra, fast iteration.

---

## Overview
- **Stack:** FastAPI, SQLModel, httpx, BackgroundTasks
- **Storage:** SQLite + local `data/` folder
- **Canvas Auth:** Personal Access Token via `.env`
- **Transcript/Summary:** fake providers + LLM stub (OpenAI optional)

---

## Models
```py
Course(id, name, last_synced_at)
Module(id, course_id, title, position, last_synced_at)
Item(id, module_id, type, title, canvas_url, provider, status, error)
Artifact(id, item_id, kind, path, created_at)
# status = DISCOVERED | TRANSCRIPT_READY | SUMMARY_READY | FAILED
Endpoints
Browse

GET /health

GET /me/courses

POST /me/courses/refresh → fetch Canvas courses

GET /courses/{id}

GET /courses/{id}/modules

POST /courses/{id}/modules/refresh

GET /modules/{id}/items

GET /items/{id} (includes transcript/summary paths)

Actions

POST /items/{id}/fetch-transcript

POST /items/{id}/summarize

Each action → runs BackgroundTasks to write files & update DB.

Canvas Client
canvas_client.py

Uses httpx + Authorization: Bearer TOKEN

Paginated fetch for courses/modules/items

Infer provider from URL: panopto / zoom / None

Transcript Provider
providers.py

FakeProvider.fetch(item) → returns dummy transcript

resolve_provider(item) chooses provider (Panopto/Zoom)

TODO: Playwright integration later

Summarizer
summarizer.py

If no OPENAI_API_KEY: return simple mock summary

Else: call OpenAI ChatCompletion with “concise markdown notes” prompt

Storage Helpers
storage.py

data/transcripts/{item_id}.txt

data/summaries/{item_id}.md

Settings
settings.py

py
Copy code
CANVAS_BASE_URL
CANVAS_TOKEN
OPENAI_API_KEY (optional)
DATA_DIR=./data
Directory Layout
pgsql
Copy code
backend/
  main.py
  models.py
  schemas.py
  deps.py
  settings.py
  canvas_client.py
  providers.py
  summarizer.py
  storage.py
  pyproject.toml
  .env.example
data/
  transcripts/
  summaries/
Behavior Summary
POST /me/courses/refresh → caches Canvas data locally

POST /courses/{id}/modules/refresh → fetches modules/items

POST /items/{id}/fetch-transcript → writes transcript file

POST /items/{id}/summarize → writes summary markdown

GET /items/{id} → shows paths + status for polling

Acceptance
Runs via uvicorn main:app --reload

SQLite auto-creates tables

Background tasks update DB + files