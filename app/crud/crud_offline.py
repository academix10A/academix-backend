from sqlalchemy.orm import Session, joinedload
from datetime import datetime
from app.models.offline import Offline


def descargar_recurso(db: Session, id_usuario: int, id_recurso: int):
    existente = db.query(Offline).filter(
        Offline.id_usuario == id_usuario,
        Offline.id_recurso == id_recurso
    ).first()

    if existente:
        existente.activo = True
        existente.ultima_sincronizacion = datetime.utcnow()
        db.commit()
        db.refresh(existente)
        return existente

    nuevo = Offline(
        id_usuario=id_usuario,
        id_recurso=id_recurso
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def obtener_descargas(db: Session, id_usuario: int):
    return db.query(Offline).options(
        joinedload(Offline.recurso)
    ).filter(
        Offline.id_usuario == id_usuario,
        Offline.activo == True
    ).all()


def eliminar_descarga(db: Session, id_usuario: int, id_recurso: int):
    registro = db.query(Offline).filter(
        Offline.id_usuario == id_usuario,
        Offline.id_recurso == id_recurso
    ).first()

    if not registro:
        return None

    registro.activo = False
    registro.ultima_sincronizacion = datetime.utcnow()

    db.commit()
    return registro