from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime
import re
from html import escape


class PublicacionBase(BaseModel):
    titulo: Optional[str] = Field(None, min_length=5, max_length=250)
    descripcion: Optional[str] = Field(None, min_length=5, max_length=500)
    texto: Optional[str] = Field(None, min_length=5, max_length=10000)
    id_usuario: Optional[int] = Field(None, gt=0, description="ID del usuario debe ser positivo")
    id_estado: Optional[int] = Field(None, gt=0, description="ID del estado debe ser positivo")
    
    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza el título de la publicación"""
        if v is None:
            return v
        
        # Eliminar espacios extras
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        # Validar longitud después de limpiar
        if len(v) < 5:
            raise ValueError('El título debe tener al menos 5 caracteres')
        
        # Permitir letras, números, espacios, acentos, guiones, paréntesis y puntuación básica
        if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-_.,;:()¿?¡!&"\']+$', v):
            raise ValueError('El título contiene caracteres no permitidos')
        
        # Escapar HTML para prevenir XSS
        v = escape(v)
        
        return v
    
    @field_validator('descripcion')
    @classmethod
    def sanitizar_descripcion(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza la descripción de la publicación"""
        if v is None:
            return v
        
        # Eliminar espacios extras
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        # Validar longitud después de limpiar
        if len(v) < 10:
            raise ValueError('La descripción debe tener al menos 10 caracteres')
        
        # Bloquear etiquetas HTML peligrosas y scripts
        if re.search(r'<script|<iframe|<object|<embed|javascript:|onerror=|onclick=|onload=', v, re.IGNORECASE):
            raise ValueError('Contenido no permitido en la descripción')
        
        # Escapar HTML
        v = escape(v)
        
        return v
    
    @field_validator('texto')
    @classmethod
    def sanitizar_texto(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza el texto completo de la publicación"""
        if v is None:
            return v
        
        # Eliminar espacios extras (pero preservar saltos de línea dobles para párrafos)
        v = v.strip()
        # Reemplazar múltiples espacios por uno solo
        v = re.sub(r' +', ' ', v)
        # Limitar saltos de línea consecutivos a máximo 2
        v = re.sub(r'\n\s*\n\s*\n+', '\n\n', v)
        
        # Validar longitud después de limpiar
        if len(v) < 5:
            raise ValueError('El texto debe tener al menos 20 caracteres')
        
        # Bloquear código malicioso y etiquetas peligrosas
        patrones_peligrosos = [
            r'<script', r'</script>', 
            r'<iframe', r'</iframe>',
            r'<object', r'</object>',
            r'<embed', r'</embed>',
            r'javascript:',
            r'onerror\s*=',
            r'onclick\s*=',
            r'onload\s*=',
            r'onmouseover\s*=',
            r'<link.*stylesheet',
            r'@import',
            r'vbscript:',
            r'data:text/html'
        ]
        
        for patron in patrones_peligrosos:
            if re.search(patron, v, re.IGNORECASE):
                raise ValueError('Contenido no permitido detectado en el texto')
        
        # Escapar HTML
        v = escape(v)
        
        return v


class PublicacionCreate(BaseModel):
    titulo: str = Field(..., min_length=5, max_length=250, description="Título de la publicación")
    descripcion: str = Field(..., min_length=5, max_length=500, description="Descripción breve")
    texto: str = Field(..., min_length=5, max_length=10000, description="Contenido completo de la publicación")
    id_usuario: int = Field(..., gt=0, description="ID del usuario autor")
    id_estado: int = Field(..., gt=0, description="ID del estado de la publicación")
    
    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v: str) -> str:
        """Sanitiza el título de la publicación"""
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        if len(v) < 5:
            raise ValueError('El título debe tener al menos 5 caracteres')
        
        if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-_.,;:()¿?¡!&"\']+$', v):
            raise ValueError('El título contiene caracteres no permitidos')
        
        v = escape(v)
        
        return v
    
    @field_validator('descripcion')
    @classmethod
    def sanitizar_descripcion(cls, v: str) -> str:
        """Sanitiza la descripción de la publicación"""
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        if len(v) < 10:
            raise ValueError('La descripción debe tener al menos 10 caracteres')
        
        if re.search(r'<script|<iframe|<object|<embed|javascript:|onerror=|onclick=|onload=', v, re.IGNORECASE):
            raise ValueError('Contenido no permitido en la descripción')
        
        v = escape(v)
        
        return v
    
    @field_validator('texto')
    @classmethod
    def sanitizar_texto(cls, v: str) -> str:
        """Sanitiza el texto completo de la publicación"""
        v = v.strip()
        v = re.sub(r' +', ' ', v)
        v = re.sub(r'\n\s*\n\s*\n+', '\n\n', v)
        
        if len(v) < 5:
            raise ValueError('El texto debe tener al menos 20 caracteres')
        
        # Bloquear código malicioso
        patrones_peligrosos = [
            r'<script', r'</script>', 
            r'<iframe', r'</iframe>',
            r'<object', r'</object>',
            r'<embed', r'</embed>',
            r'javascript:',
            r'onerror\s*=',
            r'onclick\s*=',
            r'onload\s*=',
            r'onmouseover\s*=',
            r'<link.*stylesheet',
            r'@import',
            r'vbscript:',
            r'data:text/html'
        ]
        
        for patron in patrones_peligrosos:
            if re.search(patron, v, re.IGNORECASE):
                raise ValueError('Contenido no permitido detectado en el texto')
        
        v = escape(v)
        
        return v


class PublicacionUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=5, max_length=250)
    descripcion: Optional[str] = Field(None, min_length=5, max_length=500)
    texto: Optional[str] = Field(None, min_length=5, max_length=10000)
    id_usuario: Optional[int] = Field(None, gt=0)
    id_estado: Optional[int] = Field(None, gt=0)
    
    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza el título si está presente"""
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        if len(v) < 5:
            raise ValueError('El título debe tener al menos 5 caracteres')
        
        if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-_.,;:()¿?¡!&"\']+$', v):
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
        
        if re.search(r'<script|<iframe|<object|<embed|javascript:|onerror=|onclick=|onload=', v, re.IGNORECASE):
            raise ValueError('Contenido no permitido en la descripción')
        
        v = escape(v)
        
        return v
    
    @field_validator('texto')
    @classmethod
    def sanitizar_texto(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza el texto si está presente"""
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r' +', ' ', v)
        v = re.sub(r'\n\s*\n\s*\n+', '\n\n', v)
        
        if len(v) < 5:
            raise ValueError('El texto debe tener al menos 5 caracteres')
        
        patrones_peligrosos = [
            r'<script', r'</script>', 
            r'<iframe', r'</iframe>',
            r'<object', r'</object>',
            r'<embed', r'</embed>',
            r'javascript:',
            r'onerror\s*=',
            r'onclick\s*=',
            r'onload\s*=',
            r'onmouseover\s*=',
            r'<link.*stylesheet',
            r'@import',
            r'vbscript:',
            r'data:text/html'
        ]
        
        for patron in patrones_peligrosos:
            if re.search(patron, v, re.IGNORECASE):
                raise ValueError('Contenido no permitido detectado en el texto')
        
        v = escape(v)
        
        return v


class Publicacion(PublicacionBase):
    id_publicacion: int
    fecha_creacion: datetime
    
    class Config:
        from_attributes = True