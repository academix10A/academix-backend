from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class VistaContenidoBase(BaseModel):
    id_usuario: int
    id_recurso: Optional[int] = None
    id_publicacion: Optional[int] = None


class VistaContenidoCreate(VistaContenidoBase):
    pass


class VistaContenido(VistaContenidoBase):
    id_vista: int
    fecha_vista: datetime

    class Config:
        from_attributes = True