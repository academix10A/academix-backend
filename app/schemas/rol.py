from pydantic import BaseModel
from typing import Optional

class RolBase(BaseModel):
    nombre: Optional[str] = None

class RolCreate(RolBase):
    nombre: str
    
class RolUpdate(RolBase):
    pass

class Rol(RolBase):
    id_rol: int
    
    class Config:
        from_attributes = True