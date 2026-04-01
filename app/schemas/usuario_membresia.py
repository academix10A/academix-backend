from pydantic import BaseModel
from datetime import datetime

class UsuarioMembresia(BaseModel):
    id_usuario_membresia: int
    id_usuario: int
    id_membresia: int
    fecha_inicio: datetime
    fecha_fin: datetime | None
    activa: bool

    class Config:
        orm_mode = True