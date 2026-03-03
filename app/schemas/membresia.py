from pydantic import BaseModel, Field
from typing import Optional, List
from app.schemas.beneficio import Beneficio


class MembresiaBase(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=150)
    descripcion: Optional[str] = Field(None, max_length=200)
    costo: Optional[int] = Field(None, ge=0)
    tipo: Optional[str] = Field(None, min_length=2, max_length=150)
    duracion_dias: Optional[int] = Field(None, gt=0)


class MembresiaCreate(MembresiaBase):
    nombre: str
    descripcion: str
    costo: int
    tipo: str
    duracion_dias: int
    beneficios_ids: List[int] = []


class MembresiaUpdate(MembresiaBase):
    beneficios_ids: Optional[List[int]] = None


class Membresia(BaseModel):
    id_membresia: int
    nombre: str
    descripcion: str
    costo: int
    tipo: str
    duracion_dias: int
    beneficios: List[Beneficio] = []

    class Config:
        from_attributes = True