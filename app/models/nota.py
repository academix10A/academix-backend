# app/models/nota.py
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime


class Nota(Base):
    __tablename__ = "nota"

    id_nota              = Column(Integer, primary_key=True, index=True)
    titulo               = Column(String(255), nullable=False)
    contenido            = Column(Text, nullable=False)

    fecha_creacion       = Column(DateTime, default=datetime.utcnow, nullable=False)
    fecha_actualizacion  = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )
    es_compartida        = Column(Boolean, default=False, nullable=False)

    # Claves foráneas
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False, index=True)
    id_recurso = Column(Integer, ForeignKey("recurso.id_recurso"), nullable=False, index=True)

    # Relaciones
    usuario = relationship("Usuario", back_populates="notas")
    recurso = relationship("Recurso", back_populates="notas")