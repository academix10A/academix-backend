# routers/Notas.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db, get_current_active_user
from app.crud import crud_nota
from app.schemas.nota import Nota, NotaCreate, NotaUpdate
from app.models.usuario import Usuario
from app.core.permissions import PermissionChecker

router = APIRouter(prefix="/notas", tags=["Notas"])

solo_admin = PermissionChecker(roles=["admin"])
usuarios_activos = PermissionChecker(membresias=["premium", "gratis"])


@router.get("/usuario")
def obtener_notas_usuario(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene todas las notas del usuario actual (privadas + compartidas)."""
    notas = crud_nota.get_notas_usuario(db, id_usuario=current_user.id_usuario, skip=skip, limit=limit)
    return notas


@router.get("/usuario/privadas")
def obtener_notas_privadas_usuario(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene solo las notas privadas del usuario actual."""
    notas = crud_nota.get_notas_privadas_usuario(db, id_usuario=current_user.id_usuario, skip=skip, limit=limit)
    return notas


@router.get("/usuario/compartidas")
def obtener_notas_compartidas_usuario(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene las notas compartidas del usuario actual."""
    notas = crud_nota.get_notas_compartidas_usuario(db, id_usuario=current_user.id_usuario, skip=skip, limit=limit)
    return notas


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
def create_nota(
    nota_in: NotaCreate, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Crea un nuevo Nota."""
    # Validar que no exista Nota con ese contenido
    nota_exists = crud_nota.get_nota_by_contenido(db, contenido=nota_in.contenido)
    if nota_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un nota con ese contenido"
        )
    
    # Crear la nota usando el id_usuario del token
    nota = crud_nota.create_nota(db, nota_in=nota_in, id_usuario=current_user.id_usuario)
    return nota


@router.put("/{nota_id}", response_model=Nota)
def update_nota(
    nota_id: int, 
    nota_in: NotaUpdate, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Actualiza un Nota existente verificando propiedad."""
    nota = crud_nota.get_nota(db, nota_id=nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrado")
    
    # Verificar que el usuario actual es el propietario
    if nota.id_usuario != current_user.id_usuario:
        raise HTTPException(
            status_code=403, 
            detail="No tienes permiso para modificar esta nota"
        )
    
    nota = crud_nota.update_nota(db, nota_id=nota_id, nota_in=nota_in)
    return nota


@router.delete("/{nota_id}", response_model=Nota)
def delete_nota(
    nota_id: int, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Elimina un Nota verificando propiedad."""
    nota = crud_nota.get_nota(db, nota_id=nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrado")
    
    # Verificar que el usuario actual es el propietario
    if nota.id_usuario != current_user.id_usuario:
        raise HTTPException(
            status_code=403, 
            detail="No tienes permiso para eliminar esta nota"
        )
    
    nota = crud_nota.delete_nota(db, nota_id=nota_id)
    return nota
