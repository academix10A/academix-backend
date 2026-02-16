from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import deps
from app.core.security import ALGORITHM, create_access_token
from app.schemas.token import Token
from app.crud import crud_usuario
from functools import wraps
from fastapi import HTTPException, Depends
from app.models.usuario import Usuario
from app.api.deps import get_current_user
from app.core.permissions import is_admin, has_role


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
    access_token = create_access_token(
        subject=str(user.id_usuario), expires_delta=access_token_expires,
        extra_data={
            "email": user.correo,
            "rol": user.rol.nombre if user.rol else None  
        }
    )
    return Token(access_token=access_token, token_type="bearer")

def require_admin(
    current_user: Usuario = Depends(get_current_user)
):
    """
    Dependency que SOLO permite admins.
    Uso: @router.get("/admin-only", dependencies=[Depends(require_admin)])
    """
    if not is_admin(current_user):
        raise HTTPException(
            status_code=403,
            detail="Se requieren permisos de administrador"
        )
    return current_user


def require_role(role_name: str):
    """
    Dependency factory - crea un verificador de rol específico.
    Uso: @router.get("/algo", dependencies=[Depends(require_role("premium"))])
    """
    def role_checker(current_user: Usuario = Depends(get_current_user)):
        if not has_role(current_user, role_name):
            raise HTTPException(
                status_code=403,
                detail=f"Se requiere rol: {role_name}"
            )
        return current_user
    
    return role_checker


def require_any_role(*roles: str):
    """
    Permite CUALQUIERA de los roles especificados.
    Uso: @router.get("/algo", dependencies=[Depends(require_any_role("admin", "premium"))])
    """
    def role_checker(current_user: Usuario = Depends(get_current_user)):
        if not any(has_role(current_user, role) for role in roles):
            raise HTTPException(
                status_code=403,
                detail=f"Se requiere uno de estos roles: {', '.join(roles)}"
            )
        return current_user
    
    return role_checker