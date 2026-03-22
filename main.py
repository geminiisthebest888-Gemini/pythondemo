"""Main entry point for the application."""

import os
from dotenv import load_dotenv
from openai import OpenAI

def main() -> None:
    """Run the main application."""
    load_dotenv()

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )

    model = "anthropic/claude-sonnet-4"

    message = client.chat.completions.create(
        model=model,
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": "What is quantum computing? Answer in one sentence"
            }
        ]
    )
    print(message.choices[0].message.content)

if __name__ == "__main__":
    main()
