from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Estado(Base):
    id_estado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    
    # Relaciones
    recursos = relationship("Recurso", back_populates="estado")
    publicaciones = relationship("Publicacion", back_populates="estado")
    usuarios = relationship("Usuario", back_populates="estado")
    membresias = relationship("Membresia", back_populates="estado")