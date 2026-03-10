from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_active_user
from app.models.usuario import Usuario
from app.crud import crud_vista_contenido

router = APIRouter(prefix="/vistas", tags=["Vistas"])


@router.get("/usuario/recursos")
def obtener_vistas_recursos_usuario(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene todos los recursos vistos por el usuario actual."""
    from app.models.vista_contenido import VistaContenido
    
    vistas = db.query(VistaContenido).filter(
        VistaContenido.id_usuario == current_user.id_usuario,
        VistaContenido.id_recurso.isnot(None)
    ).order_by(VistaContenido.fecha_vista.desc()).offset(skip).limit(limit).all()
    
    return vistas


@router.get("/usuario/publicaciones")
def obtener_vistas_publicaciones_usuario(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene todas las publicaciones vistas por el usuario actual."""
    from app.models.vista_contenido import VistaContenido
    
    vistas = db.query(VistaContenido).filter(
        VistaContenido.id_usuario == current_user.id_usuario,
        VistaContenido.id_publicacion.isnot(None)
    ).order_by(VistaContenido.fecha_vista.desc()).offset(skip).limit(limit).all()
    
    return vistas


@router.get("/usuario/recientes")
def obtener_contenido_reciente_usuario(
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene el contenido visto recientemente por el usuario actual."""
    from app.models.vista_contenido import VistaContenido
    
    vistas = db.query(VistaContenido).filter(
        VistaContenido.id_usuario == current_user.id_usuario
    ).order_by(VistaContenido.fecha_vista.desc()).limit(limit).all()
    
    return vistas


@router.post("/recurso/{id_recurso}")
def registrar_vista_recurso(
    id_recurso: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):

    vista = crud_vista_contenido.registrar_vista_recurso(
        db,
        current_user.id_usuario,
        id_recurso
    )

    return {"message": "vista registrada"}


@router.post("/publicacion/{id_publicacion}")
def registrar_vista_publicacion(
    id_publicacion: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):

    vista = crud_vista_contenido.registrar_vista_publicacion(
        db,
        current_user.id_usuario,
        id_publicacion
    )

    return {"message": "vista registrada"}