from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.crud import crud_usuario_membresia
from app.schemas.usuario_membresia import UsuarioMembresia
from typing import List

router = APIRouter(prefix="/usuario_membresia", tags=["Usuario Membresia"])


@router.get("/usuario/{id_usuario}", response_model=UsuarioMembresia)
def get_membresia_usuario(id_usuario: int, db: Session = Depends(get_db)):
    membresia = crud_usuario_membresia.get_membresia_by_usuario(db, id_usuario)

    if not membresia:
        raise HTTPException(
            status_code=404,
            detail="Membresía no encontrada"
        )

    return membresia

@router.get("/", response_model=List[UsuarioMembresia])
def list_membresias(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todas las membresías"""
    membresias = crud_usuario_membresia.get_membresias(db, skip=skip, limit=limit)
    return membresias