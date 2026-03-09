from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Membresia(Base):
    __tablename__ = "membresia"
    
    id_membresia = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)
    precio = Column(Float, nullable=False, default=0.0)
    
    # Relaciones
    usuarios_membresias = relationship("UsuarioMembresia", back_populates="membresia")