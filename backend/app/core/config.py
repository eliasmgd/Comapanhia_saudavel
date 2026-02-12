from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Companhia Saudável API"
    environment: str = "development"
    secret_key: str = "change-me"
    database_url: str = "sqlite:///./companhia_saudavel.db"
    access_token_expire_minutes: int = 120
    frontend_url: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
