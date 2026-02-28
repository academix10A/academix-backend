# routers/Notas.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_nota
from app.schemas.nota import Nota, NotaCreate, NotaUpdate
from app.core.permissions import PermissionChecker

router = APIRouter(prefix="/notas", tags=["Notas"])

solo_admin = PermissionChecker(roles=["admin"])
usuarios_activos = PermissionChecker(membresias=["premium", "gratis"])

@router.get("/", response_model=List[Nota])
def list_notas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los Notas con paginación."""
    notas = crud_nota.get_notas(db, skip=skip, limit=limit)
    return notas

@router.get("/contenido/{contenido}", response_model=Nota)
def get_nota_by_contenido(contenido: str, db: Session = Depends(get_db)):
    """Obtiene un nota por contenido."""
    nota = crud_nota.get_nota_by_contenido(db, contenido=contenido)
    if not nota:
        raise HTTPException(
            status_code=404, 
            detail=f"Recurso '{nota}' no encontrado"
        )
    return nota

@router.get("/{nota_id}", response_model=Nota)
def read_Nota(nota_id: int, db: Session = Depends(get_db)):
    """Obtiene un Nota por ID."""
    nota = crud_nota.get_nota(db, nota_id=nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrado")
    return nota



@router.post("/", response_model=Nota, status_code=201)
def create_nota(nota_in: NotaCreate, db: Session = Depends(get_db)):
    """Crea un nuevo Nota."""
    # Validar que no exista Nota con ese contenido
    nota_exists = crud_nota.get_nota_by_contenido(db, contenido=nota_in.contenido)
    if nota_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un nota con ese contenido"
        )
    
    nota = crud_nota.create_nota(db, nota_in=nota_in)
    return nota


@router.put("/{nota_id}", response_model=Nota)
def update_nota(
    nota_id: int, 
    nota_in: NotaUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un Nota existente."""
    nota = crud_nota.update_nota(db, nota_id=nota_id, nota_in=nota_in)
    if not nota:
        raise HTTPException(status_code=404, detail="nota no encontrado")
    return nota


@router.delete("/{nota_id}", response_model=Nota)
def delete_nota(nota_id: int, db: Session = Depends(get_db)):
    """Elimina un Nota."""
    nota = crud_nota.delete_nota(db, nota_id=nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrado")
    return nota