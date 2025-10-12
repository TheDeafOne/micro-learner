# Canvas Summarization Frontend

TypeScript + Vite frontend that connects to the FastAPI backend in this repository. It provides an interactive dashboard for browsing Canvas courses, inspecting modules and items, and launching transcript/summary jobs.

## Tech Stack

- React 19 with functional components
- Tailwind CSS with shadcn/ui primitives (`Button`, `Badge`, `Card`, `Tabs`, etc.)
- Vite build tooling (`npm run dev` / `npm run build`)

## Prerequisites

- Node.js 18+ (tested with v24)
- npm 9+ (comes with Node)
- Backend API running locally or accessible via HTTP

Install dependencies once per clone:

```bash
npm install
```

## Configuration

The app expects the backend API URL through `VITE_API_BASE_URL`. Copy the example file and adjust if your backend runs elsewhere:

```bash
cp .env.example .env
```

Defaults to `http://127.0.0.1:8000`.

## Available Scripts

| Command          | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| `npm run dev`    | Launches Vite dev server with HMR (default on `http://localhost:5173`). |
| `npm run build`  | Type-checks and builds the production bundle into `dist/`.   |
| `npm run preview`| Serves the production build locally for smoke-testing.       |

## UI Highlights

- **Course / Module explorer** – refresh Canvas data and drill into modules and items.
- **Item filters** – search by title, provider, and job status.
- **Job controls** – queue transcript and summary background tasks per item.
- **Real-time updates** – websocket connection refreshes statuses as transcripts/summaries finish.
- **Artifacts** – quick links to download generated transcripts and summaries.

All API interactions reuse the backend endpoints documented in `../README.md`. Ensure environment variables for the backend are configured and the server is running before starting the frontend.
