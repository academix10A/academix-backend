# Preguntas.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_pregunta
from app.schemas.pregunta import Pregunta, PreguntaCreate, PreguntaUpdate

router = APIRouter(prefix="/pregunta", tags=["Preguntas"])

@router.get("/", response_model=List[Pregunta])
def list_preguntas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los Preguntas con paginación."""
    preguntas = crud_pregunta.get_preguntas(db, skip=skip, limit=limit)
    return preguntas

@router.get("/contenido/{contenido}", response_model=Pregunta)
def get_pregunta_by_contenido(contenido: str, db: Session = Depends(get_db)):
    """Obtiene un pregunta por contenido."""
    pregunta = crud_pregunta.get_pregunta_by_contenido(db, contenido=contenido)
    if not pregunta:
        raise HTTPException(
            status_code=404, 
            detail=f"Pregunta '{pregunta}' no encontrado"
        )
    return pregunta

@router.get("/{pregunta_id}", response_model=Pregunta)
def read_Pregunta(pregunta_id: int, db: Session = Depends(get_db)):
    """Obtiene un Pregunta por ID."""
    pregunta = crud_pregunta.get_pregunta(db, pregunta_id=pregunta_id)
    if not pregunta:
        raise HTTPException(status_code=404, detail="Pregunta no encontrado")
    return pregunta



@router.post("/", response_model=Pregunta, status_code=201)
def create_pregunta(pregunta_in: PreguntaCreate, db: Session = Depends(get_db)):
    """Crea un nuevo Pregunta."""
    # Validar que no exista Pregunta con ese contenido
    pregunta_exists = crud_pregunta.get_pregunta_by_contenido(db, contenido=pregunta_in.contenido)
    if pregunta_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un pregunta con contenido"
        )
    
    pregunta = crud_pregunta.create_pregunta(db, pregunta_in=pregunta_in)
    return pregunta


@router.put("/{pregunta_id}", response_model=Pregunta)
def update_pregunta(
    pregunta_id: int, 
    pregunta_in: PreguntaUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un Pregunta existente."""
    pregunta = crud_pregunta.update_pregunta(db, pregunta_id=pregunta_id, pregunta_in=pregunta_in)
    if not pregunta:
        raise HTTPException(status_code=404, detail="pregunta no encontrado")
    return pregunta


@router.delete("/{pregunta_id}", response_model=Pregunta)
def delete_pregunta(pregunta_id: int, db: Session = Depends(get_db)):
    """Elimina un Pregunta."""
    pregunta = crud_pregunta.delete_pregunta(db, pregunta_id=pregunta_id)
    if not pregunta:
        raise HTTPException(status_code=404, detail="Pregunta no encontrado")
    return pregunta