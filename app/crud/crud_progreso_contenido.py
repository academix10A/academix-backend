from sqlalchemy.orm import Session
from typing import Optional

from app.models.progreso_contenido import ProgresoContenido


def obtener_progreso_recurso(
    db: Session,
    id_usuario: int,
    id_recurso: int
) -> Optional[ProgresoContenido]:

    return db.query(ProgresoContenido).filter(
        ProgresoContenido.id_usuario == id_usuario,
        ProgresoContenido.id_recurso == id_recurso
    ).first()


def obtener_progreso_publicacion(
    db: Session,
    id_usuario: int,
    id_publicacion: int
) -> Optional[ProgresoContenido]:

    return db.query(ProgresoContenido).filter(
        ProgresoContenido.id_usuario == id_usuario,
        ProgresoContenido.id_publicacion == id_publicacion
    ).first()


def actualizar_progreso_recurso(
    db: Session,
    id_usuario: int,
    id_recurso: int,
    porcentaje: float,
    posicion: Optional[int],
    completado: bool
):

    progreso = obtener_progreso_recurso(db, id_usuario, id_recurso)

    if not progreso:

        progreso = ProgresoContenido(
            id_usuario=id_usuario,
            id_recurso=id_recurso,
            porcentaje_leido=porcentaje,
            ultima_posicion=posicion,
            completado=completado
        )

        db.add(progreso)

    else:

        progreso.porcentaje_leido = porcentaje
        progreso.ultima_posicion = posicion
        progreso.completado = completado

    db.commit()
    db.refresh(progreso)

    return progreso


def actualizar_progreso_publicacion(
    db: Session,
    id_usuario: int,
    id_publicacion: int,
    porcentaje: float,
    posicion: Optional[int],
    completado: bool
):

    progreso = obtener_progreso_publicacion(db, id_usuario, id_publicacion)

    if not progreso:

        progreso = ProgresoContenido(
            id_usuario=id_usuario,
            id_publicacion=id_publicacion,
            porcentaje_leido=porcentaje,
            ultima_posicion=posicion,
            completado=completado
        )

        db.add(progreso)

    else:

        progreso.porcentaje_leido = porcentaje
        progreso.ultima_posicion = posicion
        progreso.completado = completado

    db.commit()
    db.refresh(progreso)

    return progreso