from pydantic import BaseModel
from typing import Optional

class EstadoBase(BaseModel):
    nombre: Optional[str] = None  

class EstadoCreate(EstadoBase):
    nombre: str
    
class EstadoUpdate(EstadoBase):
    pass

class Estado(EstadoBase):
    id_estado: int
    
    class Config: 
        from_attributes = True