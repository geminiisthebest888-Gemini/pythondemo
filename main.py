"""Main entry point for the application."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

model = "stepfun/step-3.5-flash:free"
system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system=None, temperature=1.0):
    full_messages = []
    if system:
        full_messages.append({"role": "system", "content": system})
    full_messages.extend(messages)

    response = client.chat.completions.create(
        model=model,
        max_tokens=1000,
        messages=full_messages,
        temperature=temperature,
    )
    if not response.choices:
        raise ValueError("API returned no response choices")
    return response.choices[0].message.content

def main() -> None:
    """Run the main application."""
    # Start with an empty message list
    messages = []

    # Add the initial user question
    add_user_message(messages, "Define quantum computing in one sentence")

    # Get Claude's response
    answer = chat(messages, system_prompt, 1.0)
    print(answer)
    # Add Claude's response to the conversation history
    add_assistant_message(messages, answer)

    # Add a follow-up question
    add_user_message(messages, "Write another sentence")

    # Get the follow-up response with full context
    final_answer = chat(messages, system_prompt,1.0)
    print(final_answer)

if __name__ == "__main__":
    main()
