from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class IAConsulta(Base):
    __tablename__ = "ia_consulta"

    id_ia_consulta = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario", ondelete="CASCADE"), nullable=False, index=True)
    id_membresia = Column(Integer, ForeignKey("membresia.id_membresia", ondelete="SET NULL"), nullable=True)
    texto_seleccionado = Column(Text, nullable=True)
    pregunta_seguimiento = Column(Text, nullable=True)
    fecha_consulta = Column(DateTime, nullable=False, server_default=func.now(), index=True)
    estado = Column(String(20), nullable=False, default="ok")