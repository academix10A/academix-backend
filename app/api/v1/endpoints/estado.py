# estado.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_estado
from app.schemas.estado import Estado, EstadoCreate, EstadoUpdate

router = APIRouter(prefix="/estado", tags=["estados"])

@router.get("/", response_model=List[Estado])
def list_estados(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los estados con paginación."""
    estados = crud_estado.get_estados(db, skip=skip, limit=limit)
    return estados

@router.get("/nombre/{nombre}", response_model=Estado)
def get_estado_by_nombre(nombre: str, db: Session = Depends(get_db)):
    """Obtiene un estado por nombre."""
    estado = crud_estado.get_estado_by_nombre(db, nombre=nombre)
    if not estado:
        raise HTTPException(
            status_code=404, 
            detail=f"Estado '{nombre}' no encontrado"
        )
    return estado


@router.get("/{estado_id}", response_model=Estado)
def read_estado(estado_id: int, db: Session = Depends(get_db)):
    """Obtiene un estado por ID."""
    estado = crud_estado.get_estado(db, estado_id=estado_id)
    if not estado:
        raise HTTPException(status_code=404, detail="estado no encontrado")
    return estado

@router.post("/", response_model=Estado, status_code=201)
def create_estado(estado_in: EstadoCreate, db: Session = Depends(get_db)):
    """Crea un nuevo estado."""
    # Validar que no exista estado con ese nombre
    estado_exists = crud_estado.get_estado_by_nombre(db, nombre=estado_in.nombre)
    if estado_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un estado con ese nombre"
        )
    
    estado = crud_estado.create_estado(db, estado_in=estado_in)
    return estado


@router.put("/{estado_id}", response_model=Estado)
def update_estado(
    estado_id: int, 
    estado_in: EstadoUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un estado existente."""
    estado = crud_estado.update_estado(db, estado_id=estado_id, estado_in=estado_in)
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    return estado


@router.delete("/{estado_id}", response_model=Estado)
def delete_estado(estado_id: int, db: Session = Depends(get_db)):
    """Elimina un estado."""
    estado = crud_estado.delete_estado(db, estado_id=estado_id)
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    return estado