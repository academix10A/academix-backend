from pydantic import BaseModel, Field, field_validator
from typing import Optional

class BeneficioBase(BaseModel):
    id_beneficio: Optional[int] = Field(None, gt=0)
    nombre: Optional[str] = Field(None, min_length=2, max_length=50)
    descripcion: Optional[str] = Field(None, max_length=200)


class BeneficioCreate(BeneficioBase):
    nombre: str = Field(..., min_length=2, max_length=50, description="Nombre del beneficio")
    descripcion: str = Field(..., max_length=200, description="Descripción del beneficio")


    @field_validator("id_beneficio")
    def validar_id_beneficio(cls, v: int):
        if v < 1:
            raise ValueError("El ID del beneficio debe ser mayor a 0")
        return v
    
class BeneficioUpdate(BeneficioBase):
    id_beneficio: Optional[int] = Field(None, gt=0, description="ID del beneficio (debe existir)")
    nombre: Optional[str] = Field(None, min_length=2, max_length=50, description="Nombre del beneficio")
    descripcion: Optional[str] = Field(None, max_length=200, description="Descripción del beneficio")

    
class Beneficio(BaseModel):
        id_beneficio: int
        nombre: str
        descripcion: str
    
        
        class Config:
            from_attributes = True