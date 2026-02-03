from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_active_user
from app.crud import crud_usuario
from app.models.usuario import Usuario as UsuarioModel
from app.schemas.usuario import Usuario, UsuarioCreate, UsuarioUpdate


router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.get("/", response_model=List[Usuario])
def list_usuarios(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: UsuarioModel = Depends(get_current_active_user)  # Requiere auth
):
    """Lista todos los usuarios con paginación. Requiere autenticación."""
    usuarios = crud_usuario.get_usuarios(db, skip=skip, limit=limit)
    return usuarios


@router.get("/me", response_model=Usuario)
def read_usuario_me(
    current_user: UsuarioModel = Depends(get_current_active_user)
):
    """Obtiene el usuario actual (perfil)."""
    return current_user


@router.get("/{id_usuario}", response_model=Usuario)
def read_usuario(
    id_usuario: int, 
    db: Session = Depends(get_db),
    current_user: UsuarioModel = Depends(get_current_active_user)
):
    """Obtiene un usuario por ID. Requiere autenticación."""
    usuario = crud_usuario.get_usuario(db, id_usuario=id_usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario no encontrado"
        )
    return usuario


@router.post("/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
def create_usuario(
    usuario_in: UsuarioCreate, 
    db: Session = Depends(get_db)
):
    """Crea un nuevo usuario. No requiere autenticación (registro público)."""
    # Validar que no exista usuario con ese correo
    usuario_exists = crud_usuario.get_usuario_by_correo(db, correo=usuario_in.correo)
    if usuario_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un usuario con ese correo electrónico"
        )
    
    usuario = crud_usuario.create_usuario(db, usuario_in=usuario_in)
    return usuario


@router.put("/{id_usuario}", response_model=Usuario)
def update_usuario(
    id_usuario: int,
    usuario_in: UsuarioUpdate,
    db: Session = Depends(get_db),
    current_user: UsuarioModel = Depends(get_current_active_user)
):
    """Actualiza un usuario existente. Solo el propio usuario puede actualizarse."""
    # Verificar que el usuario actual solo pueda actualizar su propio perfil
    if current_user.id_usuario != id_usuario:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para actualizar este usuario"
        )
    
    usuario = crud_usuario.update_usuario(db, id_usuario=id_usuario, usuario_in=usuario_in)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario no encontrado"
        )
    return usuario


@router.delete("/{id_usuario}", response_model=Usuario)
def delete_usuario(
    id_usuario: int,
    db: Session = Depends(get_db),
    current_user: UsuarioModel = Depends(get_current_active_user)
):
    """Elimina un usuario. Solo el propio usuario puede eliminarse."""
    # Verificar que el usuario actual solo pueda eliminar su propio perfil
    if current_user.id_usuario != id_usuario:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para eliminar este usuario"
        )
    
    usuario = crud_usuario.delete_usuario(db, id_usuario=id_usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario no encontrado"
        )
    return usuario