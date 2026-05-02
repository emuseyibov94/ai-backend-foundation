# Lux AI Document Intelligence

Production-ready AI document intelligence platform focused on financial, legal, and enterprise documents.

## Current Features

- FastAPI application structure
- Health check endpoint
- Pydantic response schema
- Basic test coverage

## Tech Stack

- Python
- FastAPI
- Pydantic
- Pytest

## Run Locally

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Open API docs:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/health
```

## Run Tests

```bash
pytest
```