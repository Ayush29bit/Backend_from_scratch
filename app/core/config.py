from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Backend From First Principles"
    environment: str = "dev"

    database_url: str
    redis_url: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
