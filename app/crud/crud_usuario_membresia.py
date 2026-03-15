from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.models.usuario_membresia import UsuarioMembresia
from app.models.membresia import Membresia


def crear_usuario_membresia(
    db: Session,
    id_usuario: int,
    id_membresia: int
) -> UsuarioMembresia:

    membresia = db.query(Membresia).filter(
        Membresia.id_membresia == id_membresia
    ).first()

    if not membresia:
        raise ValueError("La membresía no existe")

    fecha_inicio = datetime.utcnow()
    fecha_fin = fecha_inicio + timedelta(days=membresia.duracion_dias)

    # Desactivar membresías activas anteriores
    db.query(UsuarioMembresia).filter(
        UsuarioMembresia.id_usuario == id_usuario,
        UsuarioMembresia.activa == True
    ).update({"activa": False})

    nueva = UsuarioMembresia(
        id_usuario=id_usuario,
        id_membresia=id_membresia,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        activa=True
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva