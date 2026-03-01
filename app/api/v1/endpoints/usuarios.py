
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Request, Query
from sqlalchemy.orm import Session
import logging
from datetime import datetime

from app.api.deps import get_db, get_current_active_user
from app.crud import crud_usuario
from app.models.usuario import Usuario as UsuarioModel
from app.schemas.usuario import (
    Usuario, 
    UsuarioPublico,
    UsuarioCreate, 
    UsuarioUpdate,
    UsuarioConRol
)
from app.core.permissions import PermissionChecker

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

request_tracker = {}

def check_rate_limit(request: Request, max_requests: int = 10, window_seconds: int = 60):

    client_ip = request.client.host
    current_time = datetime.utcnow()
    
    if client_ip not in request_tracker:
        request_tracker[client_ip] = []
    
    # Limpiar requests antiguos
    request_tracker[client_ip] = [
        req_time for req_time in request_tracker[client_ip]
        if (current_time - req_time).total_seconds() < window_seconds
    ]
    
    # Verificar límite
    if len(request_tracker[client_ip]) >= max_requests:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Demasiadas solicitudes. Máximo {max_requests} por {window_seconds} segundos."
        )
    
    # Registrar request
    request_tracker[client_ip].append(current_time)


def validar_paginacion(skip: int, limit: int) -> tuple:
    if skip < 0:
        skip = 0
    
    if limit <= 0:
        limit = 10
    elif limit > 100:  # Máximo 100 para prevenir sobrecarga
        limit = 100
    
    return skip, limit

@router.get("/", response_model=List[UsuarioPublico])
def listar_usuarios(
    request: Request,
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(100, ge=1, le=100, description="Número máximo de registros"),
    id_estado: Optional[int] = Query(None, gt=0, description="Filtrar por estado"),
    id_rol: Optional[int] = Query(None, gt=0, description="Filtrar por rol"),
    id_membresia: Optional[int] = Query(None, gt=0, description="Filtrar por membresia"),
    db: Session = Depends(get_db),
    current_user: UsuarioModel = Depends(get_current_active_user)
):
    
    check_rate_limit(request, max_requests=30, window_seconds=60)
    
    # Validar paginación
    skip, limit = validar_paginacion(skip, limit)
    
    # Log de acción
    logger.info(f"Usuario {current_user.id_usuario} listando usuarios (skip={skip}, limit={limit})")
    
    # Obtener usuarios
    usuarios = crud_usuario.get_usuarios(
        db, 
        skip=skip, 
        limit=limit,
        id_estado=id_estado,
        id_rol=id_rol,
        id_membresia=id_membresia
    )
    
    return usuarios


@router.get("/me", response_model=UsuarioPublico)
def obtener_perfil_actual(
    current_user: UsuarioModel = Depends(get_current_active_user)
):
    logger.info(f"Usuario {current_user.id_usuario} consultó su propio perfil")
    return current_user


@router.get("/count", response_model=dict)
def contar_usuarios(
    id_estado: Optional[int] = Query(None, gt=0),
    id_rol: Optional[int] = Query(None, gt=0),
    db: Session = Depends(get_db),
    current_user: UsuarioModel = Depends(get_current_active_user)
):

    total = crud_usuario.count_usuarios(db, id_estado=id_estado, id_rol=id_rol)
    return {"total": total}


@router.get("/{id_usuario}", response_model=UsuarioPublico)
def obtener_usuario_por_id(
    id_usuario: int,
    db: Session = Depends(get_db),
    current_user: UsuarioModel = Depends(get_current_active_user)
):
    if id_usuario <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID de usuario inválido"
        )
    
    usuario = crud_usuario.get_usuario(db, usuario_id=id_usuario)
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    
    logger.info(f"Usuario {current_user.id_usuario} consultó usuario {id_usuario}")
    return usuario


@router.post("/", response_model=UsuarioPublico, status_code=status.HTTP_201_CREATED)
def crear_usuario(
    request: Request,
    usuario_in: UsuarioCreate,
    db: Session = Depends(get_db)
):

    check_rate_limit(request, max_requests=5, window_seconds=60)
    
    logger.info(f"Intento de registro desde IP {request.client.host} para correo {usuario_in.correo}")
    
    # El CRUD hace todas las validaciones (incluyendo que id_estado exista)
    usuario = crud_usuario.create_usuario(db, usuario_in=usuario_in)
    
    logger.info(f"Usuario creado: {usuario.id_usuario} - {usuario.correo} - Estado: {usuario.id_estado}")
    
    return usuario

@router.put("/{id_usuario}", response_model=UsuarioPublico)
def actualizar_usuario(
    id_usuario: int,
    usuario_in: UsuarioUpdate,
    db: Session = Depends(get_db),
    current_user: UsuarioModel = Depends(get_current_active_user)
):
    if id_usuario <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID de usuario inválido"
        )
    
    # Verificar permisos: Solo el usuario puede actualizarse a sí mismo
    
    if current_user.id_usuario != id_usuario:
        logger.warning(
            f"Usuario {current_user.id_usuario} intentó actualizar usuario {id_usuario} sin permisos"
        )
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para actualizar este usuario"
        )
    
    # Actualizar
    usuario = crud_usuario.update_usuario(db, usuario_id=id_usuario, usuario_in=usuario_in)
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    
    logger.info(f"Usuario {id_usuario} actualizado por {current_user.id_usuario}")
    
    return usuario


@router.patch("/{id_usuario}/cambiar-contrasena", response_model=dict)
def cambiar_contrasena(
    id_usuario: int,
    contrasena_actual: str = Query(..., min_length=1),
    contrasena_nueva: str = Query(..., min_length=8),
    db: Session = Depends(get_db),
    current_user: UsuarioModel = Depends(get_current_active_user)
):

    if id_usuario <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID de usuario inválido"
        )
    
    # Verificar permisos
    if current_user.id_usuario != id_usuario:
        logger.warning(
            f"Usuario {current_user.id_usuario} intentó cambiar contraseña de {id_usuario}"
        )
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para cambiar la contraseña de este usuario"
        )
    
    # Cambiar contraseña (valida contraseña actual)
    crud_usuario.cambiar_contrasena(
        db,
        usuario_id=id_usuario,
        contrasena_actual=contrasena_actual,
        contrasena_nueva=contrasena_nueva
    )
    
    logger.info(f"Usuario {id_usuario} cambió su contraseña exitosamente")
    
    return {"message": "Contraseña actualizada exitosamente"}


@router.delete("/{id_usuario}", response_model=UsuarioPublico)
def eliminar_usuario(
    id_usuario: int,
    db: Session = Depends(get_db),
    current_user: UsuarioModel = Depends(get_current_active_user)
):
    if id_usuario <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID de usuario inválido"
        )
    
    # Verificar permisos
    if current_user.id_usuario != id_usuario:
        logger.warning(
            f"Usuario {current_user.id_usuario} intentó eliminar usuario {id_usuario} sin permisos"
        )
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para eliminar este usuario"
        )
    
    # Soft delete (marca como inactivo)
    usuario = crud_usuario.soft_delete_usuario(db, usuario_id=id_usuario)
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    
    logger.info(f"Usuario {id_usuario} desactivado por {current_user.id_usuario}")
    
    return usuario

@router.get("/buscar/correo/{correo}", response_model=UsuarioPublico)
def buscar_usuario_por_correo(
    correo: str,
    db: Session = Depends(get_db),
    current_user: UsuarioModel = Depends(get_current_active_user)
):
    if not correo or not correo.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Correo inválido"
        )
    
    usuario = crud_usuario.get_usuario_by_correo(db, correo=correo)
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado con ese correo"
        )
    
    logger.info(f"Usuario {current_user.id_usuario} buscó usuario por correo: {correo}")
    
    return usuario
