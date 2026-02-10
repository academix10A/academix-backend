from pydantic import BaseModel
from typing import Optional

class SubtemaBase(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    nivel_dificultad: Optional[str] = None
    
class SubtemaCreate(SubtemaBase):
    nombre: str
    descripcion: str
    nivel_dificultad: str
    
class SubtemaUpdate(SubtemaBase):
    pass

class Subtema(SubtemaBase):
    id_subtema: int
    
    class Config: 
        from_attributes = True