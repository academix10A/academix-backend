from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re
from html import escape


class ExamenBase(BaseModel):
    titulo: Optional[str] = Field(None, min_length=3, max_length=200)
    descripcion: Optional[str] = Field(None, min_length=10, max_length=1000)
    cantidad_preguntas: Optional[int] = Field(None, gt=0, le=100, description="Cantidad de preguntas debe ser entre 1 y 100")
    id_subtema: Optional[int] = Field(None, gt=0, description="ID del subtema debe ser positivo")
    
    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza el título del examen"""
        if v is None:
            return v
        
        # Eliminar espacios extras
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        # Validar longitud después de limpiar
        if len(v) < 3:
            raise ValueError('El título debe tener al menos 3 caracteres')
        
        # Permitir letras, números, espacios, acentos, guiones, paréntesis y puntuación básica
        if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-_.,;:()¿?¡!]+$', v):
            raise ValueError('El título contiene caracteres no permitidos')
        
        # Escapar HTML para prevenir XSS
        v = escape(v)
        
        return v
    
    @field_validator('descripcion')
    @classmethod
    def sanitizar_descripcion(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza la descripción del examen"""
        if v is None:
            return v
        
        # Eliminar espacios extras
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        # Validar longitud después de limpiar
        if len(v) < 10:
            raise ValueError('La descripción debe tener al menos 10 caracteres')
        
        # Permitir más caracteres en descripción (permite saltos de línea representados como \n)
        # Bloquear etiquetas HTML y scripts
        if re.search(r'<script|<iframe|javascript:|onerror=|onclick=', v, re.IGNORECASE):
            raise ValueError('Contenido no permitido en la descripción')
        
        # Escapar HTML
        v = escape(v)
        
        return v


class ExamenCreate(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=200, description="Título del examen")
    descripcion: str = Field(..., min_length=10, max_length=1000, description="Descripción del examen")
    cantidad_preguntas: int = Field(..., gt=0, le=100, description="Cantidad de preguntas debe ser entre 1 y 100")
    id_subtema: int = Field(..., gt=0, description="ID del subtema (debe existir)")
    
    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v: str) -> str:
        """Sanitiza el título del examen"""
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        if len(v) < 3:
            raise ValueError('El título debe tener al menos 3 caracteres')
        
        if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-_.,;:()¿?¡!]+$', v):
            raise ValueError('El título contiene caracteres no permitidos')
        
        v = escape(v)
        
        return v
    
    @field_validator('descripcion')
    @classmethod
    def sanitizar_descripcion(cls, v: str) -> str:
        """Sanitiza la descripción del examen"""
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        if len(v) < 10:
            raise ValueError('La descripción debe tener al menos 10 caracteres')
        
        # Bloquear código malicioso
        if re.search(r'<script|<iframe|javascript:|onerror=|onclick=', v, re.IGNORECASE):
            raise ValueError('Contenido no permitido en la descripción')
        
        v = escape(v)
        
        return v


class ExamenUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=3, max_length=200)
    descripcion: Optional[str] = Field(None, min_length=10, max_length=1000)
    cantidad_preguntas: Optional[int] = Field(None, gt=0, le=100)
    id_subtema: Optional[int] = Field(None, gt=0)
    
    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza el título si está presente"""
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        if len(v) < 3:
            raise ValueError('El título debe tener al menos 3 caracteres')
        
        if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-_.,;:()¿?¡!]+$', v):
            raise ValueError('El título contiene caracteres no permitidos')
        
        v = escape(v)
        
        return v
    
    @field_validator('descripcion')
    @classmethod
    def sanitizar_descripcion(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza la descripción si está presente"""
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        if len(v) < 10:
            raise ValueError('La descripción debe tener al menos 10 caracteres')
        
        if re.search(r'<script|<iframe|javascript:|onerror=|onclick=', v, re.IGNORECASE):
            raise ValueError('Contenido no permitido en la descripción')
        
        v = escape(v)
        
        return v


class Examen(ExamenBase):
    id_examen: int
    
    class Config: 
        from_attributes = True