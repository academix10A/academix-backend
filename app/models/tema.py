from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.intermedias import tema_subtema

class Tema(Base):
    id_tema = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(50))
    nivel_dificultad = Column(String(50)) 
    
    # Relación M:M con Subtema usando tabla intermedia
    subtemas = relationship("Subtema", secondary=tema_subtema, back_populates="temas")