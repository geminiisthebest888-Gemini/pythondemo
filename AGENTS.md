# AGENTS.md

## Project Overview

Python project with OpenRouter API integration for chat completions. Uses the OpenAI SDK with OpenRouter as the backend provider.

## Environment Setup

```bash
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file with API key
echo OPENROUTER_API_KEY=your_key_here > .env
```

## Build / Lint / Test Commands

```bash
# Run the application
python main.py

# Install dependencies
pip install -r requirements.txt

# Run with venv
.venv\Scripts\python main.py
```

**Single test execution:** This project currently has no tests configured.

**Type checking:** No type checker configured.

**Linting:** No linter configured. If adding one, use ruff:
```bash
pip install ruff
ruff check .
ruff check --fix .
```

## Code Style Guidelines

### Formatting
- Use 4 spaces for indentation (per PEP 8)
- Maximum line length: 100 characters
- Use blank lines to separate functions and classes (2 blank lines between top-level definitions)
- Use single blank lines inside functions only when it improves clarity

### Imports
- Standard library imports first, then third-party, then local
- Always use `from dotenv import load_dotenv` for environment configuration
- Group imports by type with blank lines between groups:
  ```python
  import os
  import sys
  
  from dotenv import load_dotenv
  from openai import OpenAI
  
  from . import local_module
  ```

### Type Hints
- Use type hints for all function parameters and return types
- Use `-> None` for functions that don't return a value
- Use `Optional[T]` instead of `T | None` for compatibility
- Example:
  ```python
  def chat(messages: list[dict], system: str | None = None, temperature: float = 1.0) -> str:
      ...
  ```

### Naming Conventions
- **Functions/variables:** `snake_case` (e.g., `add_user_message`, `api_key`)
- **Classes:** `PascalCase` (e.g., `MathTutor`, `APIClient`)
- **Constants:** `UPPER_SNAKE_CASE` (e.g., `MAX_TOKENS`, `DEFAULT_MODEL`)
- **Private members:** Prefix with underscore (e.g., `_private_method`)

### Error Handling
- Always validate required environment variables at startup with clear error messages:
  ```python
  api_key = os.getenv("OPENROUTER_API_KEY")
  if not api_key:
      raise ValueError("OPENROUTER_API_KEY environment variable is not set")
  ```
- Validate API responses before accessing nested fields:
  ```python
  if not response.choices:
      raise ValueError("API returned no response choices")
  return response.choices[0].message.content
  ```
- Use specific exception types; avoid bare `except:`
- Include context in error messages

### Function Design
- Keep functions focused and small (under 30 lines ideally)
- Use descriptive function names that indicate action (verb + noun)
- Document complex logic with comments only when necessary
- Functions should do one thing well

### File Organization
- One module per file preferred
- Entry point in `main.py`
- Environment configuration at module level (after imports)
- Global client initialization after env var validation

### Documentation
- Module docstring at top of each file
- Function docstrings using triple quotes for public APIs
- Inline comments only for non-obvious logic

### Security
- Never commit `.env` files or API keys
- All secrets via environment variables
- Validate inputs before use
- Use `.gitignore` to exclude sensitive files

## Project Structure

```
pythondemo/
├── .env              # API keys (gitignored)
├── .venv/            # Virtual environment (gitignored)
├── main.py           # Entry point
├── requirements.txt # Pinned dependencies
├── .gitignore        # Git exclusions
└── .claude/          # Claude Code settings
```

## Dependencies

- `python-dotenv==1.0.1` - Environment variable loading
- `openai==1.54.0` - OpenRouter API client (OpenAI-compatible)
