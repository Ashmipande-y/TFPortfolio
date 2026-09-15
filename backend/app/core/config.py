from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "TrackForge API"
    app_env: str = "development"

    database_url: str

    redis_url: str | None = None
    jwt_secret: str | None = None
    sarvam_api_key: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()