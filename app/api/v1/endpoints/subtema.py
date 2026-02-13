# subtemas.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_subtema
from app.schemas.subtema import Subtema, SubtemaCreate, SubtemaUpdate

router = APIRouter(prefix="/subtemas", tags=["Subtemas"])

@router.get("/", response_model=List[Subtema])
def list_subtemas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los subtemas con paginación."""
    subtemas = crud_subtema.get_subtemas(db, skip=skip, limit=limit)
    return subtemas

@router.get("/nombre/{nombre}", response_model=Subtema)
def get_subtema_by_nombre(nombre: str, db: Session = Depends(get_db)):
    """Obtiene un subtema por nombre."""
    subtema = crud_subtema.get_subtema_by_nombre(db, nombre=nombre)
    if not subtema:
        raise HTTPException(
            status_code=404, 
            detail=f"Subtema '{nombre}' no encontrado"
        )
    return subtema

@router.get("/{subtema_id}", response_model=Subtema)
def read_subtema(subtema_id: int, db: Session = Depends(get_db)):
    """Obtiene un subtema por ID."""
    subtema = crud_subtema.get_subtema(db, subtema_id=subtema_id)
    if not subtema:
        raise HTTPException(status_code=404, detail="subTema no encontrado")
    return subtema


@router.post("/", response_model=Subtema, status_code=201)
def create_subtema(subtema_in: SubtemaCreate, db: Session = Depends(get_db)):
    """Crea un nuevo subtema."""
    # Validar que no exista tema con ese nombre
    subtema_exists = crud_subtema.get_subtema_by_nombre(db, nombre=subtema_in.nombre)
    if subtema_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un tema con ese nombre"
        )
    
    subtema = crud_subtema.create_subtema(db, subtema_in=subtema_in)
    return subtema


@router.put("/{subtema_id}", response_model=Subtema)
def update_subtema(
    subtema_id: int, 
    subtema_in: SubtemaUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un tema existente."""
    subtema = crud_subtema.update_subtema(db, subtema_id=subtema_id, subtema_in=subtema_in)
    if not subtema:
        raise HTTPException(status_code=404, detail="Subtema no encontrado")
    return subtema


@router.delete("/{subtema_id}", response_model=Subtema)
def delete_subtema(subtema_id: int, db: Session = Depends(get_db)):
    """Elimina un subtema."""
    subtema = crud_subtema.delete_subtema(db, subtema_id=subtema_id)
    if not subtema:
        raise HTTPException(status_code=404, detail="Subtema no encontrado")
    return subtema