from pydantic import BaseModel
from typing import Optional

class TipoBase(BaseModel):
    nombre: Optional[str] = None
    
class TipoCreate(TipoBase):
    nombre: str
    
class TipoUpdate(TipoBase):
    pass   

class Tipo(TipoBase):
    id_tipo: int
    
    class Config:
        from_attributes = True