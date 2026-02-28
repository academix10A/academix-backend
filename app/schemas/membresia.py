from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime
from typing import List
from app.schemas.beneficio import Beneficio 


class MembresiaBase(BaseModel):
    id_membresia: Optional[int] = Field(None, gt=0)
    nombre: Optional[str] = Field(None, min_length=2, max_length=150)
    descripcion: Optional[str] = Field(None, max_length=200)
    costo: Optional[int]
    tipo: Optional[str] = Field(None, min_length=2, max_length=200)
    fecha_inicio: Optional[datetime] = None  
    fecha_fin: Optional[datetime] = None 
    id_usuario: Optional[int] = Field(None, gt=0)
    id_rol: Optional[int] = Field(None, gt=0)
    id_estado: Optional[int] = Field(None, gt=0)
    
class MembresiaCreate(MembresiaBase):
    nombre: str = Field(..., min_length=2, max_length=50, description="Nombre de la membresía")
    descripcion: str = Field(..., max_length=200, description="Descripción de la membresía")
    costo: int = Field(..., gt=0, description="Costo de la membresía")
    tipo: str = Field(..., min_length=2, max_length=200, description="Tipo de membresía")
    fecha_inicio: datetime = Field(..., description="Fecha de inicio de la membresía")
    fecha_fin: datetime = Field(..., description="Fecha de termino de la membresía")
    id_usuario: int = Field(..., gt=0, description="ID del usuario (debe existir)")
    id_rol: int = Field(..., gt=0, description="ID del rol (debe existir)")
    id_estado: int = Field(..., gt=0, description="ID del estado (debe existir)")
    beneficios_ids: List[int] = Field(default=[], description="IDs de beneficios a asociar")
    

class MembresiaUpdate(MembresiaBase):
    id_membresia: int = Field(..., gt=0, description="ID de la membresía (debe existir)")
    nombre: Optional[str] = Field(None, min_length=2, max_length=50, description="Nombre de la membresía")
    descripcion: Optional[str] = Field(None, max_length=200, description="Descripción de la membresía")
    costo: Optional[int] = Field(None, gt=0, description="Costo de la membresía")
    tipo: Optional[str] = Field(None, min_length=2, max_length=200, description="Tipo de membresía")
    fecha_inicio: Optional[datetime] = Field(None, description="Fecha de inicio de la membresía")
    fecha_fin: Optional[datetime] = Field(None, description="Fecha de termino de la membresía")
    id_rol: Optional[int] = Field(None, gt=0, description="ID del rol (debe existir)")
    id_estado: Optional[int] = Field(None, gt=0, description="ID del estado (debe existir)")
    beneficios_ids: List[int] = Field(default=[], description="IDs de beneficios a asociar")


class Membresia(MembresiaBase):
    id_membresia: int
    nombre: str
    descripcion: str
    costo: int
    tipo: str
    beneficios: List[Beneficio] = []
    
    class Config:
        from_attributes = True

class MembresiaPublico(MembresiaBase):
    id_membresia: int
    nombre: str
    costo: int
    descripcion: str
    tipo: str
    id_usuario: int
    id_rol: int
    id_estado: int
    fecha_inicio: datetime
    fecha_fin: datetime
    beneficios: List[Beneficio] = []
    
    class Config:
        from_attributes = True