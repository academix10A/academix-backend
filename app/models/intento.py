from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime
from app.models.intermedias import respuesta_intento

class Intento(Base):
    id_intento = Column(Integer, primary_key=True, index=True)
    calificacion = Column(Float, default=0.0)
    fecha = Column(DateTime, default=datetime.utcnow)
    
    # Claves foráneas
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))
    id_examen = Column(Integer, ForeignKey("examen.id_examen"))
    
    # Relaciones
    usuario = relationship("Usuario", back_populates="intentos")
    examen = relationship("Examen", back_populates="intentos")
    respuestas = relationship("Opcion", secondary=respuesta_intento)