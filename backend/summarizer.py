from __future__ import annotations

from textwrap import shorten

from .settings import Settings


def summarize_transcript(transcript: str, settings: Settings) -> str:
    if not transcript.strip():
        raise ValueError("Transcript is empty")

    if not settings.openai_api_key:
        excerpt = shorten(transcript.replace("\n", " "), width=280, placeholder="...")
        return "\n".join(
            [
                "# Summary",
                "",
                f"- Auto-generated summary placeholder based on transcript excerpt:",
                f"  - {excerpt}",
                "",
                "_Set OPENAI_API_KEY for real LLM summaries._",
            ]
        )

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("openai package is required for LLM summaries") from exc

    client = OpenAI(api_key=settings.openai_api_key, base_url=settings.openai_base_url)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.3,
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that writes concise markdown lecture notes.",
            },
            {
                "role": "user",
                "content": "Create concise markdown notes summarizing this transcript:\n\n" + transcript,
            },
        ],
    )
    content = response.choices[0].message.content if response.choices else ""
    if not content:
        raise RuntimeError("OpenAI response did not include summary content")
    return content.strip()
