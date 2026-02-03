from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    nombre: Optional[str] = None
    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None
    correo: Optional[EmailStr] = None
    estado: Optional[str] = None
    id_rol: Optional[int] = None
    
class UsuarioCreate(UsuarioBase):
    # Atributos obligatorios para crear
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    correo: EmailStr
    contrasena: str  
    id_rol: int
        
class UsuarioUpdate(UsuarioBase):
    pass
    
class Usuario(UsuarioBase):
    id_usuario: int
    contrasena_hash: str
    fecha_registro: datetime
    
    class Config:
        from_attributes = True
    