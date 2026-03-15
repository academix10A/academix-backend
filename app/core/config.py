from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuración principal de la aplicación."""

    PROJECT_NAME: str = "core_academix"
    DATABASE_URL: str = "mysql+pymysql://root:arath07@localhost:3306/academix1"
    SECRET_KEY: str = "ZeroTwo"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()