from datetime import datetime, timedelta
from typing import Any, Union
import hashlib

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

# Configuración mejorada de passlib para evitar el error
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=12,
    bcrypt__ident="2b",
    bcrypt__default_rounds=12
)

ALGORITHM = "HS256"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica que una contraseña coincida con su hash."""
    # Truncar contraseñas largas usando SHA256
    password_bytes = plain_password.encode('utf-8')
    if len(password_bytes) > 72:
        plain_password = hashlib.sha256(password_bytes).hexdigest()
    
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Genera el hash de una contraseña."""
    # Truncar contraseñas largas usando SHA256
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > 72:
        password = hashlib.sha256(password_bytes).hexdigest()
    
    return pwd_context.hash(password)


def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    """Crea un token JWT con el subject (user_id) y expiración."""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)