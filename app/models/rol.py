from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Rol(Base):
    id_rol = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), index=True, nullable=False, unique=True)
    
    # Relación 1:M (Un rol puede tener muchos usuarios)
    usuarios = relationship("Usuario", back_populates="rol_rel")