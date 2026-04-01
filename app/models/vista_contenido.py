from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base_class import Base


class VistaContenido(Base):
    __tablename__ = "vista_contenido"

    id_vista = Column(Integer, primary_key=True, index=True)

    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_recurso = Column(Integer, ForeignKey("recurso.id_recurso"), nullable=True)
    id_publicacion = Column(Integer, ForeignKey("publicacion.id_publicacion"), nullable=True)

    fecha_vista = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario")
    recurso = relationship("Recurso")
    publicacion = relationship("Publicacion")