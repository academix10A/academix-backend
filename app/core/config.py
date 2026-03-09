from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuración principal de la aplicación."""

    PROJECT_NAME: str = "core_academix"
    DATABASE_URL: str = "mysql+pymysql://root:@localhost/academix"
    SECRET_KEY: str = "ZeroTwo"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 20160

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()