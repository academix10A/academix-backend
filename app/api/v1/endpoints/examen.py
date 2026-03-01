# examen.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_examen
from app.schemas.examen import Examen, ExamenCreate, ExamenUpdate
from app.core.permissions import PermissionChecker

router = APIRouter(prefix="/examen", tags=["Examenes"])

solo_admin = PermissionChecker(roles=["admin"])
usuarios_activos = PermissionChecker(membresias=["premium", "gratis"])

@router.get("/", response_model=List[Examen], dependencies=[Depends(usuarios_activos)])
def list_examen(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los examen con paginación."""
    examenes = crud_examen.get_examenes(db, skip=skip, limit=limit)
    return examenes

@router.get("/titulo/{titulo}", response_model=Examen,dependencies=[Depends(usuarios_activos)])
def get_examen_by_titulo(titulo: str, db: Session = Depends(get_db)):
    """Obtiene un examen por nombre."""
    examen = crud_examen.get_examen_by_titulo(db, titulo=titulo)
    if not examen:
        raise HTTPException(
            status_code=404, 
            detail=f"Examen '{titulo}' no encontrado"
        )
    return examen

@router.get("/{examen_id}", response_model=Examen, dependencies=[Depends(usuarios_activos)])
def read_examen(examen_id: int, db: Session = Depends(get_db)):
    """Obtiene un examen por ID."""
    examen = crud_examen.get_examen(db, examen_id=examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="examen no encontrado")
    return examen

@router.post("/", response_model=Examen, status_code=201, dependencies=[Depends(solo_admin)])
def create_examen(examen_in: ExamenCreate, db: Session = Depends(get_db)):
    """Crea un nuevo examen."""
    # Validar que no exista examen con ese titulo
    examen_exists = crud_examen.get_examen_by_titulo(db, titulo=examen_in.titulo)
    if examen_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un examen con ese titulo"
        )
    
    examen = crud_examen.create_examen(db, examen_in=examen_in)
    return examen


@router.put("/{examen_id}", response_model=Examen,  dependencies=[Depends(solo_admin)] )
def update_examen(
    examen_id: int, 
    examen_in: ExamenUpdate, 
    db: Session = Depends(get_db),

):
    """Actualiza un examen existente."""
    examen = crud_examen.update_examen(db, examen_id=examen_id, examen_in=examen_in)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")
    return examen


@router.delete("/{examen_id}", response_model=Examen,  dependencies=[Depends(solo_admin)])
def delete_examen(examen_id: int, db: Session = Depends(get_db)):
    """Elimina un examen."""
    examen = crud_examen.delete_examen(db, examen_id=examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")
    return examen