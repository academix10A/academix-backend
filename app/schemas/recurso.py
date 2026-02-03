from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.schemas.etiqueta import EtiquetaBase

class RecursoBase(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    contenido: Optional[str] = None
    url_archivo: Optional[str] = None
    id_tipo: Optional[int] = None
    id_estado: Optional[int] = None
    id_subtema: Optional[int] = None
    etiquetas: List[EtiquetaBase] = []
    
class RecursoCreate(RecursoBase):
    titulo: str
    descripcion: str
    contenido: str
    id_tipo: int
    id_estado: int
    id_subtema: int
    etiquetas: List[EtiquetaBase] = []

class RecursoUpdate(RecursoBase):
    pass 

class Recurso(RecursoBase):
    id_recurso: int
    fecha_publicacion: datetime
    
    class Config:
        from_attributes = True