from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuración principal de la aplicación.

    Los valores por defecto permiten ejecutar el proyecto sin necesidad de
    variables de entorno, pero se pueden sobreescribir mediante un archivo
    .env o variables del sistema.
    """

    PROJECT_NAME: str = "core_academix"
    DATABASE_URL: str = "mysql+pymysql://arath:arath07@localhost:3306/academix"
    SECRET_KEY: str = "ZeroTwo"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
