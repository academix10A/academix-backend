from pydantic import BaseModel
from typing import Optional

class ExamenBase(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    cantidad_preguntas: Optional[int] = None
    id_subtema: Optional[int] = None
    
class ExamenCreate(ExamenBase):
    titulo: str
    descripcion: str
    id_subtema: int
    
class ExamenUpdate(ExamenBase):
    pass

class Examen(ExamenBase):
    id_examen: int
    
    class Config: 
        from_attributes = True
