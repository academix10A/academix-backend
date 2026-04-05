from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuración principal de la aplicación."""

    PROJECT_NAME: str
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    PAYPAL_CLIENT_ID: str
    PAYPAL_CLIENT_SECRET: str
    PAYPAL_API: str

    class Config:
        env_file = ".env.backend"
        env_file_encoding = "utf-8"


settings = Settings()