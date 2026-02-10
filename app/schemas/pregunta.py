from pydantic import BaseModel
from typing import Optional

class PreguntaBase(BaseModel):
    contenido: Optional[str] = None
    id_examen: Optional[int] = None

class PreguntaCreate(PreguntaBase):
    contenido: str
    id_examen: int
    
class PreguntaUpdate(PreguntaBase):
    pass

class Pregunta(PreguntaBase):
    id_pregunta: int
    
    class Config: 
        from_attributes = True