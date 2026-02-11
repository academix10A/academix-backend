from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class IntentoBase(BaseModel):
    calificacion: Optional[float] = None
    id_usuario: Optional[int] = None
    id_examen: Optional[int] = None
    
class IntentoCreate(IntentoBase):
    calificacion: float
    id_usuario: int
    id_examen: int
    
class IntentoUpdate(IntentoBase):
    pass

class Intento(IntentoBase):
    id_intento: int
    fecha: datetime
    
    class Config: 
        from_attributes = True