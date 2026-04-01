from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime
from app.models.intermedias import membresias_beneficios

class Beneficio(Base):
    id_beneficio = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(String(250))
    
    # Relaciones
    membresias = relationship("Membresia", secondary=membresias_beneficios, back_populates="beneficios")