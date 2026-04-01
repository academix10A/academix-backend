from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProgresoContenidoBase(BaseModel):
    id_usuario: int
    id_recurso: Optional[int] = None
    id_publicacion: Optional[int] = None
    porcentaje_leido: float = 0
    ultima_posicion: Optional[int] = None
    completado: bool = False


class ProgresoContenidoUpdate(BaseModel):
    porcentaje_leido: Optional[float] = None
    ultima_posicion: Optional[int] = None
    completado: Optional[bool] = None


class ProgresoContenido(ProgresoContenidoBase):
    id_progreso: int
    fecha_actualizacion: datetime

    class Config:
        from_attributes = True