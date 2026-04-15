# app/api/v1/endpoints/publicaciones.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.api.deps import get_db, get_current_active_user
from app.crud import crud_publicacion
from app.schemas.publicacion import (
    Publicacion, PublicacionCreate, PublicacionUpdate,
    PublicacionResumen, PublicacionesResponse,
)
from app.core.permissions import PermissionChecker
from app.models.usuario import Usuario

router = APIRouter(prefix="/publicacion", tags=["Publicaciones"])

solo_admin        = PermissionChecker(roles=["admin"])
usuarios_activos  = PermissionChecker(membresias=["premium", "gratis"])


# ── GET / — listado con búsqueda y paginación ─────────────────────────────────

@router.get("/usuario")
def obtener_publicaciones_usuario(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene todas las notas del usuario actual (privadas + compartidas)."""
    publicaciones = crud_publicacion.get_publicacion_by_usuario(db, id_usuario=current_user.id_usuario, skip=skip, limit=limit)
    return publicaciones

@router.get("/", response_model=PublicacionesResponse)
def list_publicaciones(
    skip:           int            = Query(0,  ge=0),
    limit:          int            = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    """
    Lista publicaciones con filtros opcionales y paginación.
    """
    items, total = crud_publicacion.get_publicaciones(
        db,
        skip=skip,
        limit=limit,
    )
    return PublicacionesResponse(items=items, total=total, skip=skip, limit=limit)

@router.get("/filtros/", response_model=PublicacionesResponse)
def list_publicaciones(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),

    titulo: Optional[str] = None,
    nombre_usuario: Optional[str] = None,
    etiqueta: Optional[str] = None,

    db: Session = Depends(get_db),
):
    items, total = crud_publicacion.get_publicaciones_filtros(
        db,
        skip=skip,
        limit=limit,
        titulo=titulo,
        nombre_usuario=nombre_usuario,
        etiqueta=etiqueta,
        solo_publicadas=True
    )

    return PublicacionesResponse(items=items, total=total, skip=skip, limit=limit)


# ── GET /titulo/{titulo} ──────────────────────────────────────────────────────

@router.get("/titulo/{titulo}", response_model=Publicacion)
def get_publicacion_by_titulo(titulo: str, db: Session = Depends(get_db)):
    publicacion = crud_publicacion.get_publicacion_by_titulo(db, titulo=titulo)
    if not publicacion:
        raise HTTPException(status_code=404, detail=f"Publicación '{titulo}' no encontrada")
    return publicacion


# ── GET /{id} — detalle completo ──────────────────────────────────────────────

@router.get("/{publicacion_id}", response_model=Publicacion)
def read_publicacion(publicacion_id: int, db: Session = Depends(get_db)):
    publicacion = crud_publicacion.get_publicacion(db, publicacion_id=publicacion_id)
    if not publicacion:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    return publicacion


# ── POST / — crear publicación (requiere auth) ────────────────────────────────

@router.post("/", response_model=Publicacion, status_code=201)
def create_publicacion(
    publicacion_in: PublicacionCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user),
):
    """Crea una publicación. El autor se toma del token JWT."""
    # publicacion_exists = crud_publicacion.get_publicacion_by_titulo(db, titulo=publicacion_in.titulo)
    # if publicacion_exists:
    #     raise HTTPException(status_code=400, detail="Ya existe una publicación con ese título")

    return crud_publicacion.create_publicacion(
        db,
        publicacion_in=publicacion_in,
        id_usuario=current_user.id_usuario,
    )


# ── PUT /{id} — actualizar (solo el autor o admin) ────────────────────────────

@router.put("/{publicacion_id}", response_model=Publicacion)
def update_publicacion(
    publicacion_id: int,
    publicacion_in: PublicacionUpdate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user),
):
    publicacion = crud_publicacion.get_publicacion(db, publicacion_id=publicacion_id)
    if not publicacion:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")

    if publicacion.id_usuario != current_user.id_usuario and current_user.rol.nombre != "admin":
        raise HTTPException(status_code=403, detail="No tienes permiso para editar esta publicación")

    return crud_publicacion.update_publicacion(db, publicacion_id=publicacion_id, publicacion_in=publicacion_in)


# ── DELETE /{id} — eliminar (solo el autor o admin) ───────────────────────────

@router.delete("/{publicacion_id}", response_model=Publicacion)
def delete_publicacion(
    publicacion_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user),
):
    publicacion = crud_publicacion.get_publicacion(db, publicacion_id=publicacion_id)
    if not publicacion:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")

    if publicacion.id_usuario != current_user.id_usuario and current_user.rol.nombre != "admin":
        raise HTTPException(status_code=403, detail="No tienes permiso para eliminar esta publicación")

    return crud_publicacion.delete_publicacion(db, publicacion_id=publicacion_id)
