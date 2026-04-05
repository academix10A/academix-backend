# recursos.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_recursos
from app.schemas.recurso import Recurso, RecursoCreate, RecursoUpdate
from app.core.permissions import PermissionChecker, Beneficios

router = APIRouter(prefix="/recurso", tags=["Recursos"])

solo_admin = PermissionChecker(roles=["admin"])
puede_biblioteca = PermissionChecker(beneficios=[Beneficios.BIBLIOTECA])
puede_busqueda = PermissionChecker(beneficios=[Beneficios.BUSQUEDA])

@router.get("/", response_model=List[Recurso], dependencies=[Depends(puede_biblioteca)])
def list_recurso(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los recursos con paginación."""
    recursos = crud_recursos.get_recursos(db, skip=skip, limit=limit)
    return recursos

@router.get("/temas/{id_tema}/recursos", dependencies=[Depends(puede_biblioteca)])
def get_recursos_por_tema(id_tema: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return crud_recursos.get_recursos_by_tema(db, id_tema)

@router.get("/temas-con-recursos", dependencies=[Depends(puede_biblioteca)])
def get_temas_con_recursos(db: Session = Depends(get_db)):
    return crud_recursos.get_temas_recursos(db)

@router.get("/titulo/{titulo}", response_model=Recurso, dependencies=[Depends(puede_busqueda)])
def get_recurso_by_titulo(titulo: str, db: Session = Depends(get_db)):
    """Obtiene un recurso por nombre."""
    recurso = crud_recursos.get_recurso_by_titulo(db, titulo=titulo)
    if not recurso:
        raise HTTPException(
            status_code=404,
            detail=f"Recurso '{titulo}' no encontrado"
        )
    return recurso

@router.get("/contenido/{contenido}", response_model=Recurso, dependencies=[Depends(puede_busqueda)])
def get_recurso_by_contenido(contenido: str, db: Session = Depends(get_db)):
    """Obtiene un recurso por contenido."""
    recurso = crud_recursos.get_recurso_by_contenido(db, contenido=contenido)
    if not recurso:
        raise HTTPException(
            status_code=404,
            detail=f"Recurso '{contenido}' no encontrado"
        )
    return recurso

@router.get("/{recurso_id}", response_model=Recurso, dependencies=[Depends(puede_biblioteca)])
def read_recurso(recurso_id: int, db: Session = Depends(get_db)):
    """Obtiene un recurso por ID."""
    recurso = crud_recursos.get_recurso(db, recurso_id=recurso_id)
    if not recurso:
        raise HTTPException(status_code=404, detail="recurso no encontrado")
    return recurso

@router.post("/", response_model=Recurso, status_code=201, dependencies=[Depends(solo_admin)])
def create_recurso(recurso_in: RecursoCreate, db: Session = Depends(get_db)):
    """Crea un nuevo recurso."""
    recurso_exists = crud_recursos.get_recurso_by_titulo(db, titulo=recurso_in.titulo) and crud_recursos.get_recurso_by_url(db, url_archivo=recurso_in.url_archivo)
    if recurso_exists:
        raise HTTPException(
            status_code=400,
            detail="Ya existe un recurso con ese titulo y url"
        )
    recurso = crud_recursos.create_recurso(db, recurso_in=recurso_in)
    return recurso


@router.put("/{recurso_id}", response_model=Recurso, dependencies=[Depends(solo_admin)])
def update_recurso(
    recurso_id: int,
    recurso_in: RecursoUpdate,
    db: Session = Depends(get_db)
):
    """Actualiza un recurso existente."""
    recurso = crud_recursos.update_recurso(db, recurso_id=recurso_id, recurso_in=recurso_in)
    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")
    return recurso


@router.delete("/{recurso_id}", response_model=Recurso, dependencies=[Depends(solo_admin)])
def delete_recurso(recurso_id: int, db: Session = Depends(get_db)):
    """Elimina un recurso."""
    recurso = crud_recursos.delete_recurso(db, recurso_id=recurso_id)
    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")
    return recurso

@router.post("/{id_usuario}/{id_recurso}", dependencies=[Depends(puede_biblioteca)])
def agregar_favorito(
    id_usuario: int,
    id_recurso: int,
    db: Session = Depends(get_db)
):
    return crud_recursos.agregar_favorito(db, id_usuario, id_recurso)

@router.delete("/{id_usuario}/{id_recurso}", dependencies=[Depends(puede_biblioteca)])
def quitar_favorito(
    id_usuario: int,
    id_recurso: int,
    db: Session = Depends(get_db)
):
    return crud_recursos.quitar_favorito(db, id_usuario, id_recurso)

@router.get("/favoritos/{id_usuario}", dependencies=[Depends(puede_biblioteca)])
def get_favoritos(
    id_usuario: int,
    db: Session = Depends(get_db)
):
    return crud_recursos.get_favoritos(db, id_usuario)