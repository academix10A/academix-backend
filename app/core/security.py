from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(
    schemes=["argon2", "bcrypt"],
    deprecated="auto",
)

ALGORITHM = "HS256"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica que una contraseña coincida con su hash.
    Passlib detecta automáticamente si el hash es Argon2 o Bcrypt.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Genera el hash de una contraseña usando Argon2.
    Ya no necesitas el 'if len > 72' porque Argon2 maneja strings largos nativamente.
    """
    return pwd_context.hash(password)


def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None, extra_data: dict = None) -> str:
    """Crea un token JWT con el subject (user_id) y expiración."""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    
    if extra_data:
        to_encode.update(extra_data)
        
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)