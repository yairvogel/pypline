# pypline

A FastAPI application providing a simple items API and Fibonacci number calculation.

## Features

- REST API for managing items (create, read, list)
- Fibonacci number calculation endpoint
- Built with FastAPI, Pydantic, and Uvicorn

## Requirements

- Python >= 3.13

## Installation

```bash
uv sync
```

## Development

```bash
uv sync --dev
```

## Running

```bash
uv run uvicorn src.main:app --reload
```

## API Endpoints

- `GET /items` - List all items
- `GET /items/{item_id}` - Get item by ID
- `POST /items?name={name}` - Create a new item
- `GET /fib/{n}` - Calculate nth Fibonacci number

## Testing

```bash
uv run pytest
```

## Code Quality

```bash
uv run ruff check
uv run mypy src
uv run bandit -r src
```
