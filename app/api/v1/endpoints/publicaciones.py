# publicaciones.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_publicacion
from app.schemas.publicacion import Publicacion, PublicacionCreate, PublicacionUpdate
from app.core.permissions import PermissionChecker

router = APIRouter(prefix="/publicacion", tags=["Publicaciones"])

solo_admin = PermissionChecker(roles=["admin"])
usuarios_activos = PermissionChecker(membresias=["premium", "gratis"])

@router.get("/", response_model=List[Publicacion])
def list_publicacion(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los publicacion con paginación."""
    publicaciones = crud_publicacion.get_publicaciones(db, skip=skip, limit=limit)
    return publicaciones

@router.get("/titulo/{titulo}", response_model=Publicacion)
def get_publicacion_by_titulo(titulo: str, db: Session = Depends(get_db)):
    """Obtiene un publicacion por nombre."""
    publicacion = crud_publicacion.get_publicacion_by_titulo(db, titulo=titulo)
    if not publicacion:
        raise HTTPException(
            status_code=404, 
            detail=f"Publicacion '{publicacion}' no encontrado"
        )
    return publicacion

@router.get("/{publicacion_id}", response_model=Publicacion)
def read_publicacion(publicacion_id: int, db: Session = Depends(get_db)):
    """Obtiene un publicacion por ID."""
    publicacion = crud_publicacion.get_publicacion(db, publicacion_id=publicacion_id)
    if not publicacion:
        raise HTTPException(status_code=404, detail="publicacion no encontrado")
    return publicacion

@router.post("/", response_model=Publicacion, status_code=201)
def create_publicacion(publicacion_in: PublicacionCreate, db: Session = Depends(get_db)):
    """Crea un nuevo publicacion."""
    # Validar que no exista publicacion con ese titulo
    publicacion_exists = crud_publicacion.get_publicacion_by_titulo(db, titulo=publicacion_in.titulo)
    if publicacion_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un publicacion con ese titulo"
        )
    
    publicacion = crud_publicacion.create_publicacion(db, publicacion_in=publicacion_in)
    return publicacion


@router.put("/{publicacion_id}", response_model=Publicacion)
def update_publicacion(
    publicacion_id: int, 
    publicacion_in: PublicacionUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un publicacion existente."""
    publicacion = crud_publicacion.update_publicacion(db, publicacion_id=publicacion_id, publicacion_in=publicacion_in)
    if not publicacion:
        raise HTTPException(status_code=404, detail="publicacion no encontrado")
    return publicacion


@router.delete("/{publicacion_id}", response_model=Publicacion)
def delete_publicacion(publicacion_id: int, db: Session = Depends(get_db)):
    """Elimina un publicacion."""
    publicacion = crud_publicacion.delete_publicacion(db, publicacion_id=publicacion_id)
    if not publicacion:
        raise HTTPException(status_code=404, detail="publicacion no encontrado")
    return publicacion