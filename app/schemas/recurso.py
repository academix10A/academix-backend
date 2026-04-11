from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime
import re
from html import escape


class RecursoBase(BaseModel):
    """Base con campos comunes"""
    titulo: Optional[str] = Field(None, min_length=2, max_length=200)
    descripcion: Optional[str] = Field(None, max_length=500)
    contenido: Optional[str] = Field(None, max_length=200000)
    url_archivo: Optional[str] = Field(None, max_length=1000)
    external_id: Optional[str] = Field(None,  max_length=5000,description="atributo para api externa")
    id_tipo: Optional[int] = Field(None, gt=0, description="ID del tipo (1=PDF, 2=Video, 3=Audio)")
    id_estado: Optional[int] = Field(None, gt=0, description="ID del estado")
    id_subtema: Optional[int] = Field(None, gt=0, description="ID del subtema")
    
    
    @field_validator('titulo', 'descripcion', 'contenido')
    @classmethod
    def sanitizar_texto(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza textos: elimina caracteres peligrosos"""
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        v = escape(v)
        
        if len(v) < 1:
            raise ValueError('El campo no puede estar vacío')
        
        return v
    
    @field_validator('url_archivo')
    @classmethod
    def validar_url(cls, v: Optional[str]) -> Optional[str]:
        """Valida URL del archivo"""
        if v is None or v == "":
            return v
        
        v = v.strip()
        
        # Solo verificar que empiece con http/https (simple)
        if not v.startswith('http://') and not v.startswith('https://'):
            raise ValueError('La URL debe comenzar con http:// o https://')
        
        if len(v) > 1000:
            raise ValueError('La URL es demasiado larga (máximo 1000 caracteres)')
        
        return v


class RecursoCreate(BaseModel):
    """Schema para CREAR recursos"""
    
    titulo: str = Field(..., min_length=2, max_length=200, description="Título del recurso")
    descripcion: Optional[str] = Field(None, max_length=500, description="Descripción breve")
    contenido: Optional[str] = Field(None, max_length=5000, description="Contenido del recurso")
    url_archivo: str = Field(..., min_length=10, max_length=1000, description="URL del archivo")
    external_id: Optional[str] = Field(None,  max_length=5000,description="atributo para api externa")
    id_tipo: int = Field(..., gt=0, description="ID del tipo (1=PDF, 2=Video, 3=Audio)")
    id_estado: int = Field(..., gt=0, description="ID del estado (1=Activo, 2=Inactivo)")
    id_subtema: int = Field(..., gt=0, description="ID del subtema")
    id_etiqueta: Optional[int] = Field(None, gt=0, description="ID de etiqueta opcional")
    
    
    @field_validator('titulo')
    @classmethod
    def validar_titulo(cls, v: str) -> str:
        """Valida y sanitiza título"""
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        if len(v) < 2:
            raise ValueError('El título debe tener al menos 2 caracteres')
        
        v = escape(v)
        return v
    
    @field_validator('descripcion', 'contenido')
    @classmethod
    def sanitizar_texto(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza textos opcionales"""
        if v is None or v == "":
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        v = escape(v)
        
        return v
    
    @field_validator('url_archivo')
    @classmethod
    def validar_url_archivo(cls, v: str) -> str:
        """Valida URL del archivo"""
        v = v.strip()
        
        # Validar que sea HTTP o HTTPS
        if not v.startswith('http://') and not v.startswith('https://'):
            raise ValueError('La URL debe comenzar con http:// o https://')
        
        # Validar longitud
        if len(v) > 1000:
            raise ValueError('La URL es demasiado larga (máximo 1000 caracteres)')
        
        return v


class RecursoUpdate(BaseModel):
    """Schema para ACTUALIZAR recursos - Todos opcionales"""
    
    titulo: Optional[str] = Field(None, min_length=2, max_length=200)
    descripcion: Optional[str] = Field(None, max_length=500)
    contenido: Optional[str] = Field(None, max_length=5000)
    url_archivo: Optional[str] = Field(None, max_length=1000)
    external_id: Optional[str] = Field(None, max_length=5000)
    id_tipo: Optional[int] = Field(None, gt=0)
    id_estado: Optional[int] = Field(None, gt=0)
    id_subtema: Optional[int] = Field(None, gt=0)
    
    @field_validator('titulo')
    @classmethod
    def validar_titulo(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        if len(v) < 2:
            raise ValueError('El título debe tener al menos 2 caracteres')
        
        v = escape(v)
        return v
    
    @field_validator('descripcion', 'contenido')
    @classmethod
    def sanitizar_texto(cls, v: Optional[str]) -> Optional[str]:
        if v is None or v == "":
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        v = escape(v)
        
        return v
    
    @field_validator('url_archivo')
    @classmethod
    def validar_url(cls, v: Optional[str]) -> Optional[str]:
        if v is None or v == "":
            return v
        
        v = v.strip()
        
        if not v.startswith('http://') and not v.startswith('https://'):
            raise ValueError('La URL debe comenzar con http:// o https://')
        
        if len(v) > 1000:
            raise ValueError('La URL es demasiado larga')
        
        return v


class Recurso(RecursoBase):
    id_recurso: int
    fecha_publicacion: Optional[datetime] = None
    
    class Config:
        from_attributes = True



class RecursoPublico(BaseModel):
    id_recurso: int
    titulo: str
    descripcion: Optional[str] = None
    contenido: Optional[str] = None
    url_archivo: Optional[str] = None
    external_id: Optional[str] = None
    fecha_publicacion: Optional[datetime] = None
    id_tipo: int
    id_estado: int
    id_subtema: int
    
    class Config:
        from_attributes = True


class RecursoConRelaciones(RecursoPublico):
    """Schema con información de relaciones (opcional)"""
    
    nombre_tipo: Optional[str] = None
    nombre_estado: Optional[str] = None
    nombre_subtema: Optional[str] = None
    
    class Config:
        from_attributes = True