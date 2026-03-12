# from sqlalchemy import Column, Integer, String, Float
# from sqlalchemy.orm import relationship
# from app.db.base_class import Base


# class Membresia(Base):
#     __tablename__ = "membresia"
    
#     id_membresia = Column(Integer, primary_key=True, index=True)
#     nombre = Column(String(100), nullable=False)
#     descripcion = Column(String(255), nullable=True)
#     precio = Column(Float, nullable=False, default=0.0)
    
#     # Relaciones
#     usuarios_membresias = relationship("UsuarioMembresia", back_populates="membresia")

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.intermedias import membresias_beneficios

class Membresia(Base):
    __tablename__ = "membresia"

    id_membresia = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(String(250), nullable=False)
    costo = Column(Integer, nullable=False)
    tipo = Column(String(150), nullable=False)
    duracion_dias = Column(Integer, nullable=False)

    beneficios = relationship(
        "Beneficio",
        secondary=membresias_beneficios,
        back_populates="membresias"
    )

    usuarios_membresias = relationship(
        "UsuarioMembresia",
        back_populates="membresia",
        cascade="all, delete-orphan"
    )