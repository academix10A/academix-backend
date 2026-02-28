from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime
from app.models.intermedias import membresias_beneficios

class Membresia(Base):
    id_membresia = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(String(250), nullable=False)
    costo = Column(Integer, nullable=False)
    tipo = Column(String(150), nullable=False)
    fecha_inicio = Column(DateTime, default=datetime.utcnow)
    fecha_fin = Column(DateTime, nullable=True)
    
    #Clave Foranea
    id_estado = Column(Integer, ForeignKey("estado.id_estado"), default=1)
    id_rol = Column(Integer, ForeignKey("rol.id_rol"))
    
    #Relaciones
    usuarios = relationship("Usuario", back_populates="membresia")
    estado = relationship("Estado", back_populates="membresias")
    beneficios = relationship("Beneficio", secondary=membresias_beneficios, back_populates="membresias")
    roles = relationship("Rol", back_populates="membresias")
    