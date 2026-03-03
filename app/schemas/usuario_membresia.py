from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UsuarioMembresiaCreate(BaseModel):
    id_usuario: int
    id_membresia: int


class UsuarioMembresia(BaseModel):
    id_usuario_membresia: int
    id_usuario: int
    id_membresia: int
    fecha_inicio: datetime
    fecha_fin: datetime
    activa: bool

    class Config:
        from_attributes = True