# membresia.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_membresia
from app.schemas.membresia import Membresia, MembresiaCreate, MembresiaUpdate
from app.core.permissions import PermissionChecker

router = APIRouter(prefix="/membresias", tags=["Membresias"])

solo_admin = PermissionChecker(roles=["admin"])
usuarios_activos = PermissionChecker(membresias=["premium", "gratis"])

@router.get("/", response_model=List[Membresia])
def list_membresias(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los membresia con paginación."""
    membresias = crud_membresia.get_membresias(db, skip=skip, limit=limit)
    return membresias

@router.get("/nombre/{nombre}", response_model=Membresia)
def get_membresia_by_nombre(nombre: str, db: Session = Depends(get_db)):
    """Obtiene un membresia por nombre."""
    membresia = crud_membresia.get_membresia_by_nombre(db, nombre=nombre)
    if not membresia:
        raise HTTPException(
            status_code=404, 
            detail=f"Membresia '{nombre}' no encontrado"
        )
    return membresia

@router.get("/{membresia_id}", response_model=Membresia)
def read_membresia(membresia_id: int, db: Session = Depends(get_db)):
    """Obtiene un membresia por ID."""
    membresia = crud_membresia.get_membresia(db, membresia_id=membresia_id)
    if not membresia:
        raise HTTPException(status_code=404, detail="Membresia no encontrado")
    return membresia


@router.post("/", response_model=Membresia, status_code=201, dependencies=[Depends(solo_admin)])
def create_membresia(membresia_in: MembresiaCreate, db: Session = Depends(get_db)):
    """Crea un nuevo membresia."""
    # Validar que no exista tema con ese nombre
    membresia_exists = crud_membresia.get_membresia_by_nombre(db, nombre=membresia_in.nombre)
    if membresia_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe una membresia con ese nombre"
        )
    
    membresia = crud_membresia.create_membresia(db, membresia_in=membresia_in)
    return membresia


@router.put("/{membresia_id}", response_model=Membresia, dependencies=[Depends(solo_admin)])
def update_membresia(
    membresia_id: int, 
    membresia_in: MembresiaUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un tema existente."""
    membresia = crud_membresia.update_membresia(db, membresia_id=membresia_id, membresia_in=membresia_in)
    if not membresia:
        raise HTTPException(status_code=404, detail="Membresia no encontrado")
    return membresia


@router.delete("/{membresia_id}", response_model=Membresia, dependencies=[Depends(solo_admin)])
def delete_membresia(membresia_id: int, db: Session = Depends(get_db)):
    """Elimina un membresia."""
    membresia = crud_membresia.delete_membresia(db, membresia_id=membresia_id)
    if not membresia:
        raise HTTPException(status_code=404, detail="Membresia no encontrado")
    return membresia