from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class Publicacion(Base):
    id_publicacion = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(150), nullable=False)
    descripcion = Column(String(250), nullable=False)
    texto = Column(Text, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    
    # Claves foráneas
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))
    id_estado = Column(Integer, ForeignKey("estado.id_estado"))
    
    # Relaciones
    usuario = relationship("Usuario", back_populates="publicaciones")
    estado = relationship("Estado", back_populates="publicaciones")