# app/models/etiqueta.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.intermedias import recurso_etiqueta, publicacion_etiqueta


class Etiqueta(Base):
    __tablename__ = "etiqueta"

    id_etiqueta = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String(150), index=True, nullable=False, unique=True)

    # Relaciones M:M
    recursos      = relationship("Recurso",     secondary=recurso_etiqueta,     back_populates="etiquetas")
    publicaciones = relationship("Publicacion", secondary=publicacion_etiqueta, back_populates="etiquetas")