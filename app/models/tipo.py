from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Tipo(Base):
    id_tipo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), index=True, nullable=False, unique=True)
    
    # Relaciones
    recursos = relationship("Recurso", back_populates="tipo")
    
    