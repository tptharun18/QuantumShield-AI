from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


# Project Root -> QuantumShield-AI/
BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "QuantumShield AI"
    APP_VERSION: str = "0.1.0"
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = True

    # PostgreSQL
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # Neo4j
    NEO4J_URI: str
    NEO4J_USER: str
    NEO4J_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


settings = Settings()