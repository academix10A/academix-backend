# temas.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_tema
from app.schemas.tema import Tema, TemaCreate, TemaUpdate
from app.core.permissions import PermissionChecker

router = APIRouter(prefix="/temas", tags=["Temas"])

@router.get("/", response_model=List[Tema])
def list_temas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los temas con paginación."""
    temas = crud_tema.get_temas(db, skip=skip, limit=limit)
    return temas

@router.get("/nombre/{nombre}", response_model=Tema)
def get_tema_by_nombre(nombre: str, db: Session = Depends(get_db)):
    """Obtiene un estado por nombre."""
    tema = crud_tema.get_tema_by_nombre(db, nombre=nombre)
    if not tema:
        raise HTTPException(
            status_code=404, 
            detail=f"Tema '{nombre}' no encontrado"
        )
    return tema

@router.get("/{tema_id}", response_model=Tema)
def read_tema(tema_id: int, db: Session = Depends(get_db)):
    """Obtiene un tema por ID."""
    tema = crud_tema.get_tema(db, tema_id=tema_id)
    if not tema:
        raise HTTPException(status_code=404, detail="Tema no encontrado")
    return tema

@router.get("/nivel_dificultad/{nivel_dificultad}", response_model=Tema)
def get_temas_by_dificultad(nivel_dificultad: str, db: Session = Depends(get_db)):
    """Obtiene un tema por dificultad."""
    tema = crud_tema.get_temas_by_dificultad(db, nivel_dificultad=nivel_dificultad)
    if not tema:
        raise HTTPException(
            status_code=404, 
            detail=f"Tema '{nivel_dificultad}' no encontrado"
        )
    return tema


@router.post("/", response_model=Tema, status_code=201)
def create_tema(tema_in: TemaCreate, db: Session = Depends(get_db)):
    """Crea un nuevo tema."""
    # Validar que no exista tema con ese nombre
    tema_exists = crud_tema.get_tema_by_nombre(db, nombre=tema_in.nombre)
    if tema_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un tema con ese nombre"
        )
    
    tema = crud_tema.create_tema(db, tema_in=tema_in)
    return tema


@router.put("/{tema_id}", response_model=Tema)
def update_tema(
    tema_id: int, 
    tema_in: TemaUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un tema existente."""
    tema = crud_tema.update_tema(db, tema_id=tema_id, tema_in=tema_in)
    if not tema:
        raise HTTPException(status_code=404, detail="Tema no encontrado")
    return tema


@router.delete("/{tema_id}", response_model=Tema)
def delete_tema(tema_id: int, db: Session = Depends(get_db)):
    """Elimina un tema."""
    tema = crud_tema.delete_tema(db, tema_id=tema_id)
    if not tema:
        raise HTTPException(status_code=404, detail="Tema no encontrado")
    return tema