.PHONY: dev test compose-up compose-down compose-build logs logs-api logs-db logs-redis test-docker shell-api shell-db redis-ping db-psql

dev:
	uvicorn app.main:app --reload

test:
	pytest

compose-up:
	docker compose up --build

compose-up-d:
	docker compose up -d --build

compose-down:
	docker compose down

compose-build:
	docker compose build

logs:
	docker compose logs -f

logs-api:
	docker compose logs -f api

logs-db:
	docker compose logs -f postgres

logs-redis:
	docker compose logs -f redis

test-docker:
	docker compose run --rm api pytest

shell-api:
	docker exec -it lux-ai-api bash

shell-db:
	docker exec -it lux-ai-postgres bash

db-psql:
	docker exec -it lux-ai-postgres psql -U lux_user -d lux_ai

redis-ping:
	docker exec -it lux-ai-redis redis-cli ping