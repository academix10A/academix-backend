# etiqueta.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_etiqueta
from app.schemas.etiqueta import Etiqueta, EtiquetaCreate, EtiquetaUpdate
from app.core.permissions import PermissionChecker

router = APIRouter(prefix="/etiqueta", tags=["Etiquetas"])

@router.get("/", response_model=List[Etiqueta])
def list_etiqueta(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los roles con paginación."""
    etiquetas = crud_etiqueta.get_etiquetas(db, skip=skip, limit=limit)
    return etiquetas

@router.get("/nombre/{nombre}", response_model=Etiqueta)
def get_etiqueta_by_nombre(nombre: str, db: Session = Depends(get_db)):
    """Obtiene un rol por nombre."""
    etiqueta = crud_etiqueta.get_etiqueta_by_nombre(db, nombre=nombre)
    if not etiqueta:
        raise HTTPException(
            status_code=404, 
            detail=f"Rol '{nombre}' no encontrado"
        )
    return etiqueta


@router.get("/{etiqueta_id}", response_model=Etiqueta)
def read_etiqueta(etiqueta_id: int, db: Session = Depends(get_db)):
    """Obtiene un etiqueta por ID."""
    etiqueta = crud_etiqueta.get_etiqueta(db, etiqueta_id=etiqueta_id)
    if not etiqueta:
        raise HTTPException(status_code=404, detail="etiqueta no encontrado")
    return etiqueta

@router.post("/", response_model=Etiqueta, status_code=201)
def create_etiqueta(etiqueta_in: EtiquetaCreate, db: Session = Depends(get_db)):
    """Crea un nuevo etiqueta."""
    # Validar que no exista etiqueta con ese nombre
    etiqueta_exists = crud_etiqueta.get_etiqueta_by_nombre(db, nombre=etiqueta_in.nombre)
    if etiqueta_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un etiqueta con ese nombre"
        )
    
    etiqueta = crud_etiqueta.create_etiqueta(db, etiqueta_in=etiqueta_in)
    return etiqueta


@router.put("/{etiqueta_id}", response_model=Etiqueta)
def update_etiqueta(
    etiqueta_id: int, 
    etiqueta_in: EtiquetaUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un etiqueta existente."""
    etiqueta = crud_etiqueta.update_etiqueta(db, etiqueta_id=etiqueta_id, etiqueta_in=etiqueta_in)
    if not etiqueta:
        raise HTTPException(status_code=404, detail="etiqueta no encontrado")
    return etiqueta


@router.delete("/{etiqueta_id}", response_model=Etiqueta)
def delete_etiqueta(etiqueta_id: int, db: Session = Depends(get_db)):
    """Elimina un etiqueta."""
    etiqueta = crud_etiqueta.delete_etiqueta(db, etiqueta_id=etiqueta_id)
    if not etiqueta:
        raise HTTPException(status_code=404, detail="Etiqueta no encontrado")
    return etiqueta