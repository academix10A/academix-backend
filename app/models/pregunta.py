from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Pregunta(Base):
    id_pregunta = Column(Integer, primary_key=True, index=True)
    contenido = Column(String(150), nullable=False)
    
    # Clave foránea
    id_examen = Column(Integer, ForeignKey("examen.id_examen"))
    
    # Relaciones
    examen = relationship("Examen", back_populates="preguntas")
    opciones = relationship("Opcion", back_populates="pregunta")