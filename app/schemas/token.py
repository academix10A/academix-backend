from pydantic import BaseModel


class Token(BaseModel):
    """Respuesta del endpoint de login."""

    access_token: str
    token_type: str = "bearer"
