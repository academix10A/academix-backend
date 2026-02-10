from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime
from app.models.intermedias import usuario_recurso

class Usuario(Base):
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    apellido_paterno = Column(String(150), nullable=False)
    apellido_materno = Column(String(150), nullable=False)
    correo = Column(String(150), unique=True, index=True, nullable=False)
    contrasena_hash = Column(String(255), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    
    # Clave foránea
    id_rol = Column(Integer, ForeignKey("rol.id_rol"))
    id_estado = Column(Integer, ForeignKey("estado.id_estado"), default=1)
    
    # Relaciones
    rol = relationship("Rol", back_populates="usuarios")
    recursos = relationship("Recurso", secondary=usuario_recurso, back_populates="usuarios")
    notas = relationship("Nota", back_populates="usuario")
    intentos = relationship("Intento", back_populates="usuario")
    publicaciones = relationship("Publicacion", back_populates="usuario")
    estado = relationship("Estado", back_populates="usuarios")