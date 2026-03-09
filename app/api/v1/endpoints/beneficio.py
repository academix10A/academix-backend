# beneficios.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_beneficio
from app.schemas.beneficio import Beneficio, BeneficioCreate, BeneficioUpdate
from app.core.permissions import PermissionChecker

router = APIRouter(prefix="/beneficios", tags=["Beneficios"])

solo_admin = PermissionChecker(roles=["admin"])
usuarios_activos = PermissionChecker(membresias=["premium", "gratis"])

@router.get("/", response_model=List[Beneficio])
def list_beneficios(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los beneficios con paginación."""
    beneficios = crud_beneficio.get_beneficios(db, skip=skip, limit=limit)
    return beneficios

@router.get("/nombre/{nombre}", response_model=Beneficio)
def get_beneficio_by_nombre(nombre: str, db: Session = Depends(get_db)):
    """Obtiene un beneficios por nombre."""
    beneficios = crud_beneficio.get_beneficio_by_nombre(db, nombre=nombre)
    if not beneficios:
        raise HTTPException(
            status_code=404, 
            detail=f"Beneficios '{nombre}' no encontrado"
        )
    return beneficios

@router.get("/{beneficio_id}", response_model=Beneficio)
def read_beneficios(beneficio_id: int, db: Session = Depends(get_db)):
    """Obtiene un beneficios por ID."""
    beneficios = crud_beneficio.get_beneficio(db, beneficio_id=beneficio_id)
    if not beneficios:
        raise HTTPException(status_code=404, detail="Beneficios no encontrado")
    return beneficios


@router.post("/", response_model=Beneficio, status_code=201, dependencies=[Depends(solo_admin)])
def create_beneficios(beneficio_in: BeneficioCreate, db: Session = Depends(get_db)):
    """Crea un nuevo beneficios."""
    # Validar que no exista tema con ese nombre
    beneficios_exists = crud_beneficio.get_beneficio_by_nombre(db, nombre=beneficio_in.nombre)
    if beneficios_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un beneficio con ese nombre"
        )
    
    beneficios = crud_beneficio.create_beneficio(db, beneficio_in=beneficio_in)
    return beneficios


@router.put("/{beneficio_id}", response_model=Beneficio, dependencies=[Depends(solo_admin)])
def update_beneficios(
    beneficio_id: int, 
    beneficio_in: BeneficioUpdate, 
    db: Session = Depends(get_db)
):
    """Actualiza un tema existente."""
    beneficios = crud_beneficio.update_beneficio(db, beneficio_id=beneficio_id, beneficio_in=beneficio_in)
    if not beneficios:
        raise HTTPException(status_code=404, detail="Beneficios no encontrado")
    return beneficios


@router.delete("/{beneficio_id}", response_model=Beneficio, dependencies=[Depends(solo_admin)])
def delete_beneficios(beneficio_id: int, db: Session = Depends(get_db)):
    """Elimina un beneficios."""
    beneficios = crud_beneficio.delete_beneficio(db, beneficio_id=beneficio_id)
    if not beneficios:
        raise HTTPException(status_code=404, detail="Beneficios no encontrado")
    return beneficios