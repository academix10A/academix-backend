from pydantic import BaseModel
from typing import Optional

class OpcionBase(BaseModel):
    respuesta: Optional[str] = None
    es_correcta: Optional[bool] = None
    id_pregunta: Optional[int] = None

class OpcionCreate(OpcionBase):
    respuesta: str
    es_correcta: bool
    id_pregunta: int
    
class OpcionUpdate(OpcionBase):
    pass

class Opcion(OpcionBase):
    id_opcion: int
    
    class Config: 
        from_attributes = True