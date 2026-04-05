from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class Offline(Base):
    __tablename__ = "offline"
    __table_args__ = (
        UniqueConstraint("id_usuario", "id_recurso", name="uq_usuario_recurso_offline"),
    )

    id = Column(Integer, primary_key=True, index=True)

    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_recurso = Column(Integer, ForeignKey("recurso.id_recurso"), nullable=False)

    fecha_descarga = Column(DateTime, default=datetime.utcnow)
    ultima_sincronizacion = Column(DateTime, nullable=True)
    activo = Column(Boolean, default=True)

    usuario = relationship("Usuario", back_populates="offline")
    recurso = relationship("Recurso", back_populates="offline")