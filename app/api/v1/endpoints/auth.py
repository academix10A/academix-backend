from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import deps
from datetime import timedelta, datetime
from app.core.security import ALGORITHM, create_access_token
from app.schemas.token import Token
from app.crud import crud_usuario
from functools import wraps
from fastapi import HTTPException, Depends
from app.models.usuario import Usuario
from app.api.deps import get_current_active_user


router = APIRouter()


ACCESS_TOKEN_EXPIRE_MINUTES = 90


@router.post("/login/access-token", response_model=Token)
def login_access_token(
    db: Session = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    """Intercambia email y contraseña por un token de acceso JWT."""

    user = crud_usuario.authenticate(db, correo=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    def get_membresia_activa_nombre(user):
        activas = [m for m in user.membresias if m.activa and m.membresia]
        if not activas:
            return None
        activas.sort(key=lambda x: x.fecha_inicio or datetime.min, reverse=True)
        return activas[0].membresia.nombre

    # dentro de login_access_token
    nombre_membresia = get_membresia_activa_nombre(user)

    access_token = create_access_token(
        subject=str(user.id_usuario),
        expires_delta=access_token_expires,
        extra_data={
            "email": user.correo,
            "rol": user.rol.nombre if user.rol else None,
            "membresia": nombre_membresia,
        }
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post("/login/refresh-token", response_model=Token)  
def login_refresh_token(
    current_user: Usuario = Depends(get_current_active_user),  
):
    return Token(
        access_token=create_access_token(
            subject=str(current_user.id_usuario),
            extra_data={
                "email": current_user.correo,
                "rol": current_user.rol.nombre if current_user.rol else None
            }
        ),
        token_type="bearer",
    )