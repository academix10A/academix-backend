# recursos.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_recursos
from app.schemas.recurso import Recurso, RecursoCreate, RecursoUpdate

router = APIRouter(prefix="/recurso", tags=["Recursos"])

@router.get("/", response_model=List[Recurso])
def list_recurso(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los recursos con paginación."""
    recursos = crud_recursos.get_recursos(db, skip=skip, limit=limit)
    return recursos

@router.get("/titulo/{titulo}", response_model=Recurso)
def get_recurso_by_titulo(titulo: str, db: Session = Depends(get_db)):
    """Obtiene un recurso por nombre."""
    recurso = crud_recursos.get_recurso_by_titulo(db, titulo=titulo)
    if not recurso:
        raise HTTPException(
            status_code=404, 
            detail=f"Recurso '{recurso}' no encontrado"
        )
    return recurso

@router.get("/contenido/{contenido}", response_model=Recurso)
def get_recurso_by_contenido(contenido: str, db: Session = Depends(get_db)):
    """Obtiene un recurso por contenido."""
    recurso = crud_recursos.get_recurso_by_contenido(db, contenido=contenido)
    if not recurso:
        raise HTTPException(
            status_code=404, 
            detail=f"Recurso '{recurso}' no encontrado"
        )
    return recurso

@router.get("/{recurso_id}", response_model=Recurso)
def read_recurso(recurso_id: int, db: Session = Depends(get_db)):
    """Obtiene un recurso por ID."""
    recurso = crud_recursos.get_recurso(db, recurso_id=recurso_id)
    if not recurso:
        raise HTTPException(status_code=404, detail="recurso no encontrado")
    return recurso

@router.post("/", response_model=Recurso, status_code=201)
def create_recurso(recurso_in: RecursoCreate, db: Session = Depends(get_db)):
    """Crea un nuevo recurso."""
    # Validar que no exista recurso con ese titulo
    recurso_exists = crud_recursos.get_recurso_by_titulo(db, titulo=recurso_in.titulo) and crud_recursos.get_recurso_by_url(db, url_archivo=recurso_in.url_archivo)
    if recurso_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un recurso con ese titulo y url"
        )
    
    recurso = crud_recursos.create_recurso(db, recurso_in=recurso_in)
    return recurso


@router.put("/{recurso_id}", response_model=Recurso)
def update_recurso(
    recurso_id: int, 
    recurso_in: RecursoUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un recurso existente."""
    recurso = crud_recursos.update_recurso(db, recurso_id=recurso_id, recurso_in=recurso_in)
    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")
    return recurso


@router.delete("/{recurso_id}", response_model=Recurso)
def delete_recurso(recurso_id: int, db: Session = Depends(get_db)):
    """Elimina un recurso."""
    recurso = crud_recursos.delete_recurso(db, recurso_id=recurso_id)
    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")
    return recurso