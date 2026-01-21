from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    NEXTJS_BASE_URL: str
    TIMEZONE: str

    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
