from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class Nota(Base):
    id_nota = Column(Integer, primary_key=True, index=True)
    contenido = Column(String(150), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    es_compartida = Column(Boolean, default=False)
    
    # Claves foráneas
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))
    id_recurso = Column(Integer, ForeignKey("recurso.id_recurso"))
    
    # Relaciones
    usuario = relationship("Usuario", back_populates="notas")
    recurso = relationship("Recurso", back_populates="notas")