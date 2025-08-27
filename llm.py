import asyncio
from openai import AsyncOpenAI
from tqdm.asyncio import tqdm_asyncio
from dotenv import load_dotenv
import os
load_dotenv()
# Initialize the async client with your custom gateway
client = AsyncOpenAI(
    base_url=os.getenv("PORTKEY_AI_BASE_URL"),
    api_key=os.getenv("PORTKEY_AI_API_KEY")  # Replace with your actual API key
)


async def fetch_response(prompt: str):
    response = await client.chat.completions.create(
        model="gpt-5-mini",  # Change to the model you want
        messages=[{"role": "user", "content": prompt}]
    )
    return prompt, response.choices[0].message.content


async def multi_query(prompts):
    tasks = [fetch_response(p) for p in prompts]
    results = []
    for coro in tqdm_asyncio.as_completed(tasks, total=len(tasks), desc="Processing"):
        result = await coro
        results.append(result)

    return [result[1] for result in results]
