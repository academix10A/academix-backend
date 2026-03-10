from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.api.deps import get_db, get_current_active_user
from app.models.usuario import Usuario
from app.schemas.progreso_contenido import ProgresoContenidoUpdate, ProgresoContenido as ProgresoSchema
from app.crud import crud_progreso_contenido

router = APIRouter(prefix="/progreso", tags=["Progreso"])


@router.get("/usuario/recursos")
def obtener_progreso_recursos_usuario(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene el progreso de lectura de todos los recursos del usuario actual."""
    from app.models.progreso_contenido import ProgresoContenido
    
    progresos = db.query(ProgresoContenido).filter(
        ProgresoContenido.id_usuario == current_user.id_usuario,
        ProgresoContenido.id_recurso.isnot(None)
    ).order_by(ProgresoContenido.fecha_actualizacion.desc()).offset(skip).limit(limit).all()
    
    return progresos


@router.get("/usuario/publicaciones")
def obtener_progreso_publicaciones_usuario(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene el progreso de lectura de todas las publicaciones del usuario actual."""
    from app.models.progreso_contenido import ProgresoContenido
    
    progresos = db.query(ProgresoContenido).filter(
        ProgresoContenido.id_usuario == current_user.id_usuario,
        ProgresoContenido.id_publicacion.isnot(None)
    ).order_by(ProgresoContenido.fecha_actualizacion.desc()).offset(skip).limit(limit).all()
    
    return progresos


@router.get("/usuario/recurso/{id_recurso}")
def obtener_progreso_recurso_usuario(
    id_recurso: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene el progreso de un recurso específico del usuario actual."""
    progreso = crud_progreso_contenido.obtener_progreso_recurso(
        db,
        current_user.id_usuario,
        id_recurso
    )
    
    if not progreso:
        raise HTTPException(
            status_code=404,
            detail="No se encontró progreso para este recurso"
        )
    
    return progreso


@router.get("/usuario/publicacion/{id_publicacion}")
def obtener_progreso_publicacion_usuario(
    id_publicacion: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene el progreso de una publicación específica del usuario actual."""
    progreso = crud_progreso_contenido.obtener_progreso_publicacion(
        db,
        current_user.id_usuario,
        id_publicacion
    )
    
    if not progreso:
        raise HTTPException(
            status_code=404,
            detail="No se encontró progreso para esta publicación"
        )
    
    return progreso


@router.patch("/recurso/{id_recurso}")
def actualizar_progreso_recurso(
    id_recurso: int,
    progreso: ProgresoContenidoUpdate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):

    resultado = crud_progreso_contenido.actualizar_progreso_recurso(
        db,
        current_user.id_usuario,
        id_recurso,
        progreso.porcentaje_leido,
        progreso.ultima_posicion,
        progreso.completado
    )

    return resultado


@router.patch("/publicacion/{id_publicacion}")
def actualizar_progreso_publicacion(
    id_publicacion: int,
    progreso: ProgresoContenidoUpdate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):

    resultado = crud_progreso_contenido.actualizar_progreso_publicacion(
        db,
        current_user.id_usuario,
        id_publicacion,
        progreso.porcentaje_leido,
        progreso.ultima_posicion,
        progreso.completado
    )

    return resultado