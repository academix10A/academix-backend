# routers/Intentos.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_intento
from app.schemas.intento import Intento, IntentoCreate, IntentoUpdate
from app.schemas.usuario import Usuario
from app.core.permissions import PermissionChecker

router = APIRouter(prefix="/intento", tags=["Intentos"])

@router.get("/", response_model=List[Intento])
def list_intentos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los Intentos con paginación."""
    intentos = crud_intento.get_intentos(db, skip=skip, limit=limit)
    return intentos

@router.get("/calificacion/{calificacion}", response_model=Intento)
def get_intento_by_calificacion(calificacion: str, db: Session = Depends(get_db)):
    """Obtiene un intento por contenido."""
    intento = crud_intento.get_intento_by_calificacion(db, calificacion==calificacion)
    if not intento:
        raise HTTPException(
            status_code=404, 
            detail=f"Calificacion '{intento}' no encontrado"
        )
    return intento

@router.get("/{intento_id}", response_model=Intento)
def read_Intento(intento_id: int, db: Session = Depends(get_db)):
    """Obtiene un Intento por ID."""
    intento = crud_intento.get_intento(db, intento_id=intento_id)
    if not intento:
        raise HTTPException(status_code=404, detail="Intento no encontrado")
    return intento



@router.post("/", response_model=Intento, status_code=201)
def create_intento(intento_in: IntentoCreate, db: Session = Depends(get_db)):
    """Crea un nuevo Intento validando que el usuario no repita el mismo examen."""
    
    # Buscamos si ya existe un registro con el mismo usuario Y el mismo examen [cite: 199, 209]
    intento_exists = crud_intento.get_intento_by_user_and_exam(
        db, 
        id_usuario=intento_in.id_usuario, 
        id_examen=intento_in.id_examen
    )
    
    if intento_exists:
        raise HTTPException(
            status_code=400, 
            detail=f"Este '{Usuario}' ya ha realizado un intento para este examen."
        )
    
    intento = crud_intento.create_intento(db, intento_in=intento_in)
    return intento


@router.put("/{intento_id}", response_model=Intento)
def update_intento(
    intento_id: int, 
    intento_in: IntentoUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un Intento existente."""
    intento = crud_intento.update_intento(db, intento_id=intento_id, intento_in=intento_in)
    if not intento:
        raise HTTPException(status_code=404, detail="intento no encontrado")
    return intento


@router.delete("/{intento_id}", response_model=Intento)
def delete_intento(intento_id: int, db: Session = Depends(get_db)):
    """Elimina un Intento."""
    intento = crud_intento.delete_intento(db, intento_id=intento_id)
    if not intento:
        raise HTTPException(status_code=404, detail="Intento no encontrado")
    return intento