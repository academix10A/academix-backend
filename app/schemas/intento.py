from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime

class IntentoBase(BaseModel):
    calificacion: Optional[float] = None
    id_usuario: Optional[int] = None
    id_examen: Optional[int] = None
    
class IntentoCreate(IntentoBase):
    id_examen: int = Field(..., gt=0, description="ID del examen")
    respuestas: Dict[int, int] = Field(..., description="Respuestas del usuario")
    
class IntentoUpdate(IntentoBase):
    pass

class Intento(IntentoBase):
    id_intento: int
    fecha: datetime
    
    class Config: 
        from_attributes = True
