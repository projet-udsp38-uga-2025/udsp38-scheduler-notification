from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    NEXTJS_BASE_URL: str
    DATABASE_URL: str
    DEPLOYMENT_ENV: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
TIMEZONE: str = "Europe/Paris"
FIREBASE_MAIN_TOPIC = "news" + settings.DEPLOYMENT_ENV
