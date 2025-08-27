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

# Define an async function to handle a single request


async def fetch_response(prompt: str):
    response = await client.chat.completions.create(
        model="gpt-5-mini",  # Change to the model you want
        messages=[{"role": "user", "content": prompt}]
    )
    return prompt, response.choices[0].message.content

# Main async function


async def main():
    prompts = [
        "Write a haiku about space exploration.",
        "Explain quantum entanglement in simple terms.",
        "What are the main differences between TCP and UDP?",
        "Summarize the causes of World War I in one paragraph.",
        "Describe the process of nuclear fusion."
    ]

    tasks = [fetch_response(p) for p in prompts]

    results = []
    # Iterate as tasks complete, with progress bar
    for coro in tqdm_asyncio.as_completed(tasks, total=len(tasks), desc="Processing"):
        result = await coro
        results.append(result)

    # Print the results nicely
    for prompt, answer in results:
        print(f"\nPrompt: {prompt}\nResponse: {answer}\n{'-'*50}")


if __name__ == '__main__':
    asyncio.run(main())
