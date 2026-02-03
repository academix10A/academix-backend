from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base
from app.models.intermedias import usuario_recurso, recurso_etiqueta  

class Recurso(Base):  
    id_recurso = Column(Integer, primary_key=True, index=True)
    contenido = Column(String(50))
    titulo = Column(String(50), nullable=False)
    descripcion = Column(String(50))
    url_archivo = Column(String(50))
    fecha_publicacion = Column(DateTime, default=datetime.utcnow)
    
    # Claves foráneas
    id_tipo = Column(Integer, ForeignKey("tipo.id_tipo"))
    id_estado = Column(Integer, ForeignKey("estado.id_estado"))
    id_subtema = Column(Integer, ForeignKey("subtema.id_subtema"))
    
    # Relaciones M:1
    tipo = relationship("Tipo", back_populates="recursos")
    estado = relationship("Estado", back_populates="recursos")
    subtema = relationship("Subtema", back_populates="recursos")
    
    # Relaciones M:M (usando secondary)
    usuarios = relationship("Usuario", secondary=usuario_recurso, back_populates="recursos")
    etiquetas = relationship("Etiqueta", secondary=recurso_etiqueta, back_populates="recursos")
    
    # Relación 1:M
    notas = relationship("Nota", back_populates="recurso")