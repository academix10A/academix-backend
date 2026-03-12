# Opcion.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_opcion
from app.schemas.opcion import Opcion, OpcionCreate, OpcionUpdate
from app.core.permissions import PermissionChecker

router = APIRouter(prefix="/opcion", tags=["Opciones"])

solo_admin = PermissionChecker(roles=["admin"])
usuarios_activos = PermissionChecker(membresias=["premium", "gratis"])

@router.get("/", response_model=List[Opcion])
def list_opcions(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los Opciones con paginación."""
    opcions = crud_opcion.get_opciones(db, skip=skip, limit=limit)
    return opcions

@router.get("/respuesta/{respuesta}", response_model=Opcion)
def get_opcion_by_respuesta(respuesta: str, db: Session = Depends(get_db)):
    """Obtiene un opcion por contenido."""
    opcion = crud_opcion.get_opcion_by_respuesta(db, respuesta=respuesta)
    if not opcion:
        raise HTTPException(
            status_code=404, 
            detail=f"Opcion '{opcion}' no encontrado"
        )
    return opcion

@router.get("/{opcion_id}", response_model=Opcion)
def read_Opcion(opcion_id: int, db: Session = Depends(get_db)):
    """Obtiene un Opcion por ID."""
    opcion = crud_opcion.get_opcion(db, opcion_id=opcion_id)
    if not opcion:
        raise HTTPException(status_code=404, detail="Opcion no encontrado")
    return opcion



@router.post("/", response_model=Opcion, status_code=201, dependencies=[Depends(solo_admin)])
def create_opcion(opcion_in: OpcionCreate, db: Session = Depends(get_db)):
    """Crea un nuevo Opcion."""
    # Validar que no exista Opcion con respuesta
    opcion_exists = crud_opcion.get_opcion_by_respuesta(db, respuesta=opcion_in.respuesta)
    if opcion_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un opcion con ese respuesta"
        )
    
    opcion = crud_opcion.create_opcion(db, opcion_in=opcion_in)
    return opcion


@router.put("/{opcion_id}", response_model=Opcion, dependencies=[Depends(solo_admin)])
def update_opcion(
    opcion_id: int, 
    opcion_in: OpcionUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un Opcion existente."""
    opcion = crud_opcion.update_opcion(db, opcion_id=opcion_id, opcion_in=opcion_in)
    if not opcion:
        raise HTTPException(status_code=404, detail="opcion no encontrado")
    return opcion


@router.delete("/{opcion_id}", response_model=Opcion, dependencies=[Depends(solo_admin)])
def delete_opcion(opcion_id: int, db: Session = Depends(get_db)):
    """Elimina un Opcion."""
    opcion = crud_opcion.delete_opcion(db, opcion_id=opcion_id)
    if not opcion:
        raise HTTPException(status_code=404, detail="Opcion no encontrado")
    return opcion