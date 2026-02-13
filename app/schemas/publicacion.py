from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PublicacionBase(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    texto: Optional[str] = None
    id_usuario: Optional[int] = None
    id_estado: Optional[int] = None

class PublicacionCreate(PublicacionBase):
    titulo: str
    descripcion: str
    texto: str
    id_usuario: int
    id_estado: int

class PublicacionUpdate(PublicacionBase):
    pass

class Publicacion(PublicacionBase):
    id_publicacion: int
    fecha_creacion: datetime
    
    class Config:
        from_attributes = True