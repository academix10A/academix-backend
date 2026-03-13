# app/api/v1/endpoints/nota.py
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db, get_current_active_user
from app.crud import crud_nota
from app.schemas.nota import Nota, NotaCreate, NotaUpdate
from app.models.usuario import Usuario
from app.core.permissions import PermissionChecker

router = APIRouter(prefix="/notas", tags=["Notas"])



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


# ── GET /notas/  ──────────────────────────────────────────────────────────────
# Solo devuelve las notas del usuario autenticado, no las de todos
@router.get("/", response_model=List[Nota])
def list_notas(
    skip:  int = 0,
    limit: int = 100,
    db:    Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user),
):
    """Lista las notas del usuario autenticado con paginación."""
    notas = crud_nota.get_notas_by_usuario(
        db, id_usuario=current_user.id_usuario, skip=skip, limit=limit
    )
    return notas


# ── GET /notas/{nota_id}  ─────────────────────────────────────────────────────
# Solo permite ver una nota si pertenece al usuario o es compartida
@router.get("/{nota_id}", response_model=Nota)
def read_nota(
    nota_id: int,
    db:      Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user),
):
    """Obtiene una nota por ID. Solo la puede ver su dueño o si es compartida."""
    nota = crud_nota.get_nota(db, nota_id=nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")

    # Verificar acceso: dueño de la nota O nota compartida
    if nota.id_usuario != current_user.id_usuario and not nota.es_compartida:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permiso para ver esta nota",
        )
    return nota


# ── POST /notas/  ─────────────────────────────────────────────────────────────
@router.post("/", response_model=Nota, status_code=201)
def create_nota(
    nota_in: NotaCreate,
    db:      Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user),
):
    """
    Crea una nota nueva.
    - El id_usuario SIEMPRE se toma del token JWT, nunca del body.
      Esto evita que un usuario cree notas en nombre de otro.
    - Valida duplicado solo dentro de las notas del mismo usuario.
    """

    # Seguridad: ignorar el id_usuario que venga del body y usar el del token
    nota_in.id_usuario = current_user.id_usuario

    # Validar duplicado solo por usuario (no globalmente)
    nota_exists = crud_nota.get_nota_by_contenido_y_usuario(
        db,
        contenido=nota_in.contenido,
        id_usuario=current_user.id_usuario,
    )
    if nota_exists:
        raise HTTPException(
            status_code=400,
            detail="Ya tienes una nota con ese mismo contenido",
        )
    
    # # Crear la nota usando el id_usuario del token
    # nota = crud_nota.create_nota(db, nota_in=nota_in, id_usuario=current_user.id_usuario)

    nota = crud_nota.create_nota(db, nota_in=nota_in)
    return nota


# ── PUT /notas/{nota_id}  ─────────────────────────────────────────────────────
@router.put("/{nota_id}", response_model=Nota)
def update_nota(
    nota_id: int,
    nota_in: NotaUpdate,
    db:      Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user),
):
    """Actualiza una nota. Solo el dueño puede editarla."""
    nota = crud_nota.get_nota(db, nota_id=nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")

    if nota.id_usuario != current_user.id_usuario:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permiso para editar esta nota",
        )

    nota = crud_nota.update_nota(db, nota_id=nota_id, nota_in=nota_in)
    return nota


# ── DELETE /notas/{nota_id}  ──────────────────────────────────────────────────
@router.delete("/{nota_id}", response_model=Nota)
def delete_nota(
    nota_id: int,
    db:      Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user),
):
    """Elimina una nota. Solo el dueño puede eliminarla."""
    nota = crud_nota.get_nota(db, nota_id=nota_id)
    if not nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")

    if nota.id_usuario != current_user.id_usuario:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permiso para eliminar esta nota",
        )

    nota = crud_nota.delete_nota(db, nota_id=nota_id)
    return nota


# ── GET /notas/compartidas/  ─────────────────────────────────────────────────
# Endpoint público de notas compartidas (comunidad)
@router.get("/compartidas/", response_model=List[Nota])
def list_notas_compartidas(
    skip:  int = 0,
    limit: int = 100,
    db:    Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user),
):
    """Lista todas las notas marcadas como compartidas (comunidad)."""
    return crud_nota.get_notas_compartidas(db, skip=skip, limit=limit)
