from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.intermedias import recurso_etiqueta


class Etiqueta(Base):
    id_etiqueta = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), index=True, nullable=False, unique=True)
    
    # Relaciones M:M
    recursos = relationship("Recurso", secondary=recurso_etiqueta, back_populates="etiquetas")
