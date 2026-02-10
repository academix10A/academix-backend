from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NotaBase(BaseModel):
    contenido: Optional[str] = None
    es_compartida: Optional[bool] = None
    id_usuario: Optional[int] = None
    id_recurso: Optional[int] = None
    
class NotaCreate(NotaBase):
    contenido: str
    es_compartida: bool
    id_usuario: int
    id_recurso: int

class NotaUpdate(NotaBase):
    pass 

class Nota(NotaBase):
    id_nota: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    
    class Config:
        from_attributes = True