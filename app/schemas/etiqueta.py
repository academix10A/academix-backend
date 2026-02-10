from pydantic import BaseModel
from typing import Optional

class EtiquetaBase(BaseModel):
    nombre: Optional[str] = None
    
class EtiquetaCreate(EtiquetaBase):
    nombre: str
    
class EtiquetaUpdate(EtiquetaBase):
    pass 

class Etiqueta(EtiquetaBase):
    id_etiqueta: int
    
    class Config:
        from_attributes = True