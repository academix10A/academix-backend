from pydantic import BaseModel
from typing import Optional

class TemaBase(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    nivel_dificultad: Optional[str] = None
    
class TemaCreate(TemaBase):
    nombre: str
    descripcion: str
    nivel_dificultad: str
    
class TemaUpdate(TemaBase):
    pass

class Tema(TemaBase):
    id_tema: int
    
    class Config: 
        from_attributes = True