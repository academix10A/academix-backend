from sqlalchemy.orm import Session
from typing import Optional

from app.models.vista_contenido import VistaContenido


def registrar_vista_recurso(db: Session, id_usuario: int, id_recurso: int) -> VistaContenido:

    vista = db.query(VistaContenido).filter(
        VistaContenido.id_usuario == id_usuario,
        VistaContenido.id_recurso == id_recurso
    ).first()

    if vista:
        return vista

    vista = VistaContenido(
        id_usuario=id_usuario,
        id_recurso=id_recurso
    )

    db.add(vista)
    db.commit()
    db.refresh(vista)

    return vista


def registrar_vista_publicacion(db: Session, id_usuario: int, id_publicacion: int) -> VistaContenido:

    vista = db.query(VistaContenido).filter(
        VistaContenido.id_usuario == id_usuario,
        VistaContenido.id_publicacion == id_publicacion
    ).first()

    if vista:
        return vista

    vista = VistaContenido(
        id_usuario=id_usuario,
        id_publicacion=id_publicacion
    )

    db.add(vista)
    db.commit()
    db.refresh(vista)

    return vista


def contar_vistas_recurso(db: Session, id_recurso: int) -> int:

    return db.query(VistaContenido).filter(
        VistaContenido.id_recurso == id_recurso
    ).count()


def contar_vistas_publicacion(db: Session, id_publicacion: int) -> int:

    return db.query(VistaContenido).filter(
        VistaContenido.id_publicacion == id_publicacion
    ).count()