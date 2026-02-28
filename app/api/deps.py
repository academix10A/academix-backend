from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import ALGORITHM
from app.db.session import SessionLocal
from app.crud import crud_usuario
from app.models.usuario import Usuario
from sqlalchemy.orm import joinedload

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/auth/login/access-token")


def get_db() -> Generator:
    """Dependency para obtener sesión de base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




def get_current_user(
    db: Session = Depends(get_db), 
    token: str = Depends(reusable_oauth2)
) -> Usuario:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # joinedload para traer rol y membresía en la misma query — sin N+1
    user = (
        db.query(Usuario)
        .options(
            joinedload(Usuario.rol),
            joinedload(Usuario.membresia)
        )
        .filter(Usuario.id_usuario == int(user_id))
        .first()
    )
    
    if user is None:
        raise credentials_exception
    
    return user


def get_current_active_user(
    current_user: Usuario = Depends(get_current_user),
) -> Usuario:
    """Verifica que el usuario actual esté activo."""
    if not crud_usuario.is_active(current_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario inactivo"
        )
    return current_user