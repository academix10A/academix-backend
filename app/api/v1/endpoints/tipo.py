# routers/temas.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_tipo
from app.schemas.tipo import Tipo, TipoCreate, TipoUpdate

router = APIRouter(prefix="/tipo", tags=["tipos"])

@router.get("/", response_model=List[Tipo])
def list_rol(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los tipos con paginación."""
    tipos = crud_tipo.get_tipos(db, skip=skip, limit=limit)
    return tipos

@router.get("/nombre/{nombre}", response_model=Tipo)
def get_tipo_by_nombre(nombre: str, db: Session = Depends(get_db)):
    """Obtiene un tipo por nombre."""
    tipo = crud_tipo.get_tipo_by_nombre(db, nombre=nombre)
    if not tipo:
        raise HTTPException(
            status_code=404, 
            detail=f"tipo '{nombre}' no encontrado"
        )
    return tipo


@router.get("/{tipo_id}", response_model=Tipo)
def read_tipo(tipo_id: int, db: Session = Depends(get_db)):
    """Obtiene un tipo por ID."""
    tipo = crud_tipo.get_tipo(db, tipo_id=tipo_id)
    if not tipo:
        raise HTTPException(status_code=404, detail="tipo no encontrado")
    return tipo

@router.post("/", response_model=Tipo, status_code=201)
def create_tipo(tipo_in: TipoCreate, db: Session = Depends(get_db)):
    """Crea un nuevo tipo."""
    # Validar que no exista estado con ese nombre
    tipo_exists = crud_tipo.get_tipo_by_nombre(db, nombre=tipo_in.nombre)
    if tipo_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un rol con ese nombre"
        )
    
    tipo = crud_tipo.create_tipo(db, tipo_in=tipo_in)
    return tipo


@router.put("/{tipo_id}", response_model=Tipo)
def update_tipo(
    tipo_id: int, 
    tipo_in: TipoUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un rol existente."""
    tipo = crud_tipo.update_tipo(db, tipo_id=tipo_id, tipo_in=tipo_in)
    if not tipo:
        raise HTTPException(status_code=404, detail="tipo no encontrado")
    return tipo


@router.delete("/{tipo_id}", response_model=Tipo)
def delete_tipo(tipo_id: int, db: Session = Depends(get_db)):
    """Elimina un ."""
    tipo = crud_tipo.delete_tipo(db, tipo_id=tipo_id)
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo no encontrado")
    return tipo