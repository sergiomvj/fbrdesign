from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FBR-Design"
    app_env: str = "development"
    app_debug: bool = True
    api_prefix: str = "/api"
    database_url: str = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/fbr_design"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
