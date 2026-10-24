import os
from pydantic_settings import BaseSettings, SettingsConfigDict

APP_NAME = "Utsavly"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = APP_NAME
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    ai_mock: bool = os.getenv("AI_MOCK", "true").lower() in ("true", "1", "yes")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./utsavly.db")
    cors_origins: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ]

settings = Settings()
