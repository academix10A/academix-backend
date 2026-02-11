from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.intermedias import tema_subtema

class Subtema(Base):
    id_subtema = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(String(150))
    nivel_dificultad = Column(String(150))
    
    # Relaciones
    temas = relationship("Tema", secondary=tema_subtema, back_populates="subtemas")
    recursos = relationship("Recurso", back_populates="subtema")
    examenes = relationship("Examen", back_populates="subtema")