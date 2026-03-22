"""Main entry point for the application."""

import os
from dotenv import load_dotenv


def main() -> None:
    """Run the main application."""
    load_dotenv()

    # Example: access environment variables
    # api_key = os.getenv("ANTHROPIC_API_KEY")

    print("Hello, Python!")


if __name__ == "__main__":
    main()
