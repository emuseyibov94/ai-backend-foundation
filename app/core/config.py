from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "lux-ai-document-intelligence"
    app_version: str = "0.1.0"
    app_env: str = "local"
    log_level: str = "INFO"

    postgres_user: str = "lux_user"
    postgres_password: str = "lux_password"
    postgres_db: str = "lux_ai"
    postgres_host: str = "postgres"
    postgres_port: int = 5432
    database_url: str = (
        "postgresql+psycopg://lux_user:lux_password@postgres:5432/lux_ai"
    )

    redis_host: str = "redis"
    redis_port: int = 6379
    redis_db: int = 0
    redis_url: str = "redis://redis:6379/0"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()