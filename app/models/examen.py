from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Examen(Base):
    id_examen = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(50), nullable=False)
    cantidad_preguntas = Column(Integer, default=0)
    descripcion = Column(String(50))
    
    # Clave foránea
    id_subtema = Column(Integer, ForeignKey("subtema.id_subtema"))
    
    # Relaciones
    subtema = relationship("Subtema", back_populates="examenes")
    preguntas = relationship("Pregunta", back_populates="examen")
    intentos = relationship("Intento", back_populates="examen")