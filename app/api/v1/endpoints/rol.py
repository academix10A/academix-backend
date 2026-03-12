# rol.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_rol
from app.schemas.rol import Rol, RolCreate, RolUpdate
from app.core.permissions import PermissionChecker

router = APIRouter(prefix="/rol", tags=["Roles"])

@router.get("/", response_model=List[Rol])
def list_rol(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los roles con paginación."""
    roles = crud_rol.get_roles(db, skip=skip, limit=limit)
    return roles

@router.get("/nombre/{nombre}", response_model=Rol)
def get_rol_by_nombre(nombre: str, db: Session = Depends(get_db)):
    """Obtiene un rol por nombre."""
    rol = crud_rol.get_rol_by_nombre(db, nombre=nombre)
    if not rol:
        raise HTTPException(
            status_code=404, 
            detail=f"Rol '{nombre}' no encontrado"
        )
    return rol


@router.get("/{rol_id}", response_model=Rol)
def read_rol(rol_id: int, db: Session = Depends(get_db)):
    """Obtiene un rol por ID."""
    rol = crud_rol.get_rol(db, rol_id=rol_id)
    if not rol:
        raise HTTPException(status_code=404, detail="rol no encontrado")
    return rol

@router.post("/", response_model=Rol, status_code=201)
def create_rol(rol_in: RolCreate, db: Session = Depends(get_db)):
    """Crea un nuevo rol."""
    # Validar que no exista estado con ese nombre
    rol_exists = crud_rol.get_rol_by_nombre(db, nombre=rol_in.nombre)
    if rol_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un rol con ese nombre"
        )
    
    rol = crud_rol.create_rol(db, rol_in=rol_in)
    return rol


@router.put("/{rol_id}", response_model=Rol)
def update_rol(
    rol_id: int, 
    rol_in: RolUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un rol existente."""
    rol = crud_rol.update_rol(db, rol_id=rol_id, rol_in=rol_in)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol


@router.delete("/{rol_id}", response_model=Rol)
def delete_rol(rol_id: int, db: Session = Depends(get_db)):
    """Elimina un rol."""
    rol = crud_rol.delete_rol(db, rol_id=rol_id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol