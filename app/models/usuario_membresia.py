from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime


class UsuarioMembresia(Base):
    __tablename__ = "usuario_membresia"
    
    id_usuario_membresia = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_membresia = Column(Integer, ForeignKey("membresia.id_membresia"), nullable=False)
    fecha_inicio = Column(DateTime, nullable=False, default=datetime.utcnow)
    fecha_fin = Column(DateTime, nullable=True)
    activa = Column(Boolean, default=True, nullable=False)
    
    # Relaciones
    usuario = relationship("Usuario", back_populates="membresias")
    membresia = relationship("Membresia", back_populates="usuarios_membresias")