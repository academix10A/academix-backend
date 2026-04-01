from sqlalchemy import Column, Integer, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base_class import Base


class ProgresoContenido(Base):
    __tablename__ = "progreso_contenido"

    id_progreso = Column(Integer, primary_key=True, index=True)

    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_recurso = Column(Integer, ForeignKey("recurso.id_recurso"), nullable=True)
    id_publicacion = Column(Integer, ForeignKey("publicacion.id_publicacion"), nullable=True)

    porcentaje_leido = Column(Float, default=0)
    ultima_posicion = Column(Integer, nullable=True)

    completado = Column(Boolean, default=False)

    fecha_actualizacion = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    usuario = relationship("Usuario")
    recurso = relationship("Recurso")
    publicacion = relationship("Publicacion")