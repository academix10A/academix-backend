# app/models/publicacion.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Table
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime
from app.models.intermedias import publicacion_etiqueta

class Publicacion(Base):
    __tablename__ = "publicacion"

    id_publicacion = Column(Integer, primary_key=True, index=True)
    titulo         = Column(String(250), nullable=False)
    descripcion    = Column(String(500), nullable=False)
    texto          = Column(Text, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Claves foráneas
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False, index=True)
    id_estado  = Column(Integer, ForeignKey("estado.id_estado"), nullable=True)

    # Relaciones
    usuario   = relationship("Usuario",  back_populates="publicaciones", lazy="joined")
    estado    = relationship("Estado",   back_populates="publicaciones")
    etiquetas = relationship(
        "Etiqueta",
        secondary=publicacion_etiqueta,
        back_populates="publicaciones",
        lazy="joined",
    )