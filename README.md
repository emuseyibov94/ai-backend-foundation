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

## Configuration

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Example:

```env
APP_NAME=lux-ai-document-intelligence
APP_VERSION=0.1.0
APP_ENV=local
LOG_LEVEL=INFO
```

## Run with Docker

Build and start the API:

```bash
docker compose up --build
```

Open:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/health
```

Run tests inside Docker:

```bash
docker compose run --rm api pytest
```

Stop services:

```bash
docker compose down
```

## Database

This project uses PostgreSQL with pgvector for future vector search capabilities.

Start services:

```bash
docker compose up --build
```

Connect to PostgreSQL:

```bash
docker exec -it lux-ai-postgres psql -U lux_user -d lux_ai
```

Enable pgvector extension:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

Check extension:

```sql
SELECT extname FROM pg_extension WHERE extname = 'vector';
```

## Redis

This project uses Redis as the foundation for caching and future background job processing.

Start services:

```bash
docker compose up --build
```

Check Redis:

```bash
docker exec -it lux-ai-redis redis-cli ping
```

Expected response:

```text
PONG
```