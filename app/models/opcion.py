from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Opcion(Base):
    id_opcion = Column(Integer, primary_key=True, index=True)
    respuesta = Column(String(50), nullable=False)
    es_correcta = Column(Boolean, default=False)
    
    # Clave foránea
    id_pregunta = Column(Integer, ForeignKey("pregunta.id_pregunta"))
    
    # Relaciones
    pregunta = relationship("Pregunta", back_populates="opciones")