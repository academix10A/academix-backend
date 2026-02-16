from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime
import re
from html import escape


class NotaBase(BaseModel):
    contenido: Optional[str] = Field(None, min_length=1, max_length=5000)
    es_compartida: Optional[bool] = None
    id_usuario: Optional[int] = Field(None, gt=0, description="ID del usuario debe ser positivo")
    id_recurso: Optional[int] = Field(None, gt=0, description="ID del recurso debe ser positivo")
    
    @field_validator('contenido')
    @classmethod
    def sanitizar_contenido(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza el contenido de la nota"""
        if v is None:
            return v
        
        # Eliminar espacios al inicio y final
        v = v.strip()
        
        # Reemplazar múltiples espacios por uno solo (preservando estructura)
        v = re.sub(r' +', ' ', v)
        
        # Limitar saltos de línea consecutivos a máximo 3 (para notas con formato)
        v = re.sub(r'\n\s*\n\s*\n\s*\n+', '\n\n\n', v)
        
        # Validar que no esté vacío después de limpiar
        if len(v) < 1:
            raise ValueError('El contenido no puede estar vacío')
        
        # Bloquear código malicioso y etiquetas peligrosas
        patrones_peligrosos = [
            r'<script',
            r'</script>',
            r'<iframe',
            r'</iframe>',
            r'<object',
            r'</object>',
            r'<embed',
            r'</embed>',
            r'javascript:',
            r'onerror\s*=',
            r'onclick\s*=',
            r'onload\s*=',
            r'onmouseover\s*=',
            r'onmouseenter\s*=',
            r'onfocus\s*=',
            r'onblur\s*=',
            r'<link.*stylesheet',
            r'@import',
            r'vbscript:',
            r'data:text/html',
            r'<style',
            r'</style>',
            r'<form',
            r'</form>',
        ]
        
        for patron in patrones_peligrosos:
            if re.search(patron, v, re.IGNORECASE):
                raise ValueError('Contenido no permitido detectado en la nota')
        
        # Escapar HTML para prevenir XSS
        v = escape(v)
        
        return v


class NotaCreate(BaseModel):
    contenido: str = Field(..., min_length=1, max_length=5000, description="Contenido de la nota")
    es_compartida: bool = Field(..., description="Si la nota es compartida con otros usuarios")
    id_usuario: int = Field(..., gt=0, description="ID del usuario que crea la nota")
    id_recurso: int = Field(..., gt=0, description="ID del recurso asociado")
    
    @field_validator('contenido')
    @classmethod
    def sanitizar_contenido(cls, v: str) -> str:
        """Sanitiza el contenido de la nota"""
        # Eliminar espacios extras
        v = v.strip()
        v = re.sub(r' +', ' ', v)
        v = re.sub(r'\n\s*\n\s*\n\s*\n+', '\n\n\n', v)
        
        # Validar que no esté vacío después de limpiar
        if len(v) < 1:
            raise ValueError('El contenido no puede estar vacío')
        
        # Bloquear código malicioso
        patrones_peligrosos = [
            r'<script',
            r'</script>',
            r'<iframe',
            r'</iframe>',
            r'<object',
            r'</object>',
            r'<embed',
            r'</embed>',
            r'javascript:',
            r'onerror\s*=',
            r'onclick\s*=',
            r'onload\s*=',
            r'onmouseover\s*=',
            r'onmouseenter\s*=',
            r'onfocus\s*=',
            r'onblur\s*=',
            r'<link.*stylesheet',
            r'@import',
            r'vbscript:',
            r'data:text/html',
            r'<style',
            r'</style>',
            r'<form',
            r'</form>',
        ]
        
        for patron in patrones_peligrosos:
            if re.search(patron, v, re.IGNORECASE):
                raise ValueError('Contenido no permitido detectado en la nota')
        
        # Escapar HTML
        v = escape(v)
        
        return v


class NotaUpdate(BaseModel):
    contenido: Optional[str] = Field(None, min_length=1, max_length=5000)
    es_compartida: Optional[bool] = None
    id_usuario: Optional[int] = Field(None, gt=0)
    id_recurso: Optional[int] = Field(None, gt=0)
    
    @field_validator('contenido')
    @classmethod
    def sanitizar_contenido(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza el contenido si está presente"""
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r' +', ' ', v)
        v = re.sub(r'\n\s*\n\s*\n\s*\n+', '\n\n\n', v)
        
        if len(v) < 1:
            raise ValueError('El contenido no puede estar vacío')
        
        patrones_peligrosos = [
            r'<script',
            r'</script>',
            r'<iframe',
            r'</iframe>',
            r'<object',
            r'</object>',
            r'<embed',
            r'</embed>',
            r'javascript:',
            r'onerror\s*=',
            r'onclick\s*=',
            r'onload\s*=',
            r'onmouseover\s*=',
            r'onmouseenter\s*=',
            r'onfocus\s*=',
            r'onblur\s*=',
            r'<link.*stylesheet',
            r'@import',
            r'vbscript:',
            r'data:text/html',
            r'<style',
            r'</style>',
            r'<form',
            r'</form>',
        ]
        
        for patron in patrones_peligrosos:
            if re.search(patron, v, re.IGNORECASE):
                raise ValueError('Contenido no permitido detectado en la nota')
        
        v = escape(v)
        
        return v


class Nota(NotaBase):
    id_nota: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    
    class Config:
        from_attributes = True