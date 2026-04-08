# app/schemas/publicacion.py
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime
import re
from html import escape


# ── Validadores reutilizables ─────────────────────────────────────────────────

_PATRONES_PELIGROSOS = [
    r'<script', r'</script>', r'<iframe', r'</iframe>',
    r'<object', r'</object>', r'<embed', r'</embed>',
    r'javascript:', r'onerror\s*=', r'onclick\s*=', r'onload\s*=',
    r'onmouseover\s*=', r'<link.*stylesheet', r'@import',
    r'vbscript:', r'data:text/html',
]

def _sanitizar_titulo(v: str) -> str:
    v = v.strip()
    v = re.sub(r'\s+', ' ', v)
    if len(v) < 5:
        raise ValueError('El título debe tener al menos 5 caracteres')
    if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-_.,;:()¿?¡!&"\']+$', v):
        raise ValueError('El título contiene caracteres no permitidos')
    return escape(v)

def _sanitizar_texto(v: str) -> str:
    v = v.strip()
    v = re.sub(r' +', ' ', v)
    v = re.sub(r'\n\s*\n\s*\n\s*\n+', '\n\n\n', v)
    if len(v) < 5:
        raise ValueError('El texto debe tener al menos 5 caracteres')
    for patron in _PATRONES_PELIGROSOS:
        if re.search(patron, v, re.IGNORECASE):
            raise ValueError('Contenido no permitido detectado en el texto')
    return escape(v)

def _sanitizar_descripcion(v: str) -> str:
    v = v.strip()
    v = re.sub(r'\s+', ' ', v)
    if len(v) < 5:
        raise ValueError('La descripción debe tener al menos 5 caracteres')
    for patron in _PATRONES_PELIGROSOS:
        if re.search(patron, v, re.IGNORECASE):
            raise ValueError('Contenido no permitido en la descripción')
    return escape(v)


# ── Schema de usuario embebido en publicación ─────────────────────────────────

class UsuarioPublicacion(BaseModel):
    """Info mínima del autor que se devuelve junto a la publicación."""
    id_usuario: int
    nombre: str
    apellido_paterno: str

    class Config:
        from_attributes = True

    @property
    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido_paterno}"


# ── Schema de etiqueta embebida ───────────────────────────────────────────────

class EtiquetaOut(BaseModel):
    id_etiqueta: int
    nombre: str

    class Config:
        from_attributes = True


# ── Schemas de Publicación ────────────────────────────────────────────────────

class PublicacionBase(BaseModel):
    titulo: Optional[str] = Field(None, min_length=5, max_length=250)
    descripcion: Optional[str] = Field(None, min_length=5, max_length=500)
    texto: Optional[str] = Field(None, min_length=5, max_length=10000)
    id_usuario: Optional[int] = Field(None, gt=0)
    id_estado: Optional[int] = Field(None, gt=0)

    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v): return _sanitizar_titulo(v) if v else v

    @field_validator('descripcion')
    @classmethod
    def sanitizar_descripcion(cls, v): return _sanitizar_descripcion(v) if v else v

    @field_validator('texto')
    @classmethod
    def sanitizar_texto(cls, v): return _sanitizar_texto(v) if v else v


class PublicacionCreate(BaseModel):
    titulo: str = Field(..., min_length=5, max_length=250)
    descripcion: str = Field(..., min_length=5, max_length=500)
    texto: str = Field(..., min_length=5, max_length=10000)
    id_estado: int = Field(..., gt=0)
    etiquetas: Optional[List[int]] = Field(default=[], description="IDs de etiquetas a asociar")

    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v): return _sanitizar_titulo(v)

    @field_validator('descripcion')
    @classmethod
    def sanitizar_descripcion(cls, v): return _sanitizar_descripcion(v)

    @field_validator('texto')
    @classmethod
    def sanitizar_texto(cls, v): return _sanitizar_texto(v)


class PublicacionUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=5, max_length=250)
    descripcion: Optional[str] = Field(None, min_length=5, max_length=500)
    texto: Optional[str] = Field(None, min_length=5, max_length=10000)
    id_estado: Optional[int] = Field(None, gt=0)
    etiquetas: Optional[List[int]] = Field(None, description="IDs de etiquetas (reemplaza las actuales)")

    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v): return _sanitizar_titulo(v) if v else v

    @field_validator('descripcion')
    @classmethod
    def sanitizar_descripcion(cls, v): return _sanitizar_descripcion(v) if v else v

    @field_validator('texto')
    @classmethod
    def sanitizar_texto(cls, v): return _sanitizar_texto(v) if v else v


# ── Schema de respuesta enriquecida ──────────────────────────────────────────

class Publicacion(BaseModel):
    """Schema de respuesta completo con autor y etiquetas embebidas."""
    id_publicacion: int
    titulo: str
    descripcion: str
    texto: str
    fecha_creacion: datetime
    id_estado: Optional[int] = None

    # Datos del autor
    usuario: Optional[UsuarioPublicacion] = None

    # Etiquetas asociadas
    etiquetas: List[EtiquetaOut] = []

    class Config:
        from_attributes = True


class PublicacionResumen(BaseModel):
    """Schema ligero para listas (sin el texto completo)."""
    id_publicacion: int
    titulo: str
    descripcion: str
    fecha_creacion: datetime
    id_estado: Optional[int] = None
    usuario: Optional[UsuarioPublicacion] = None
    etiquetas: List[EtiquetaOut] = []

    class Config:
        from_attributes = True


class PublicacionesResponse(BaseModel):
    """Respuesta paginada de publicaciones."""
    items: List[PublicacionResumen]
    total: int
    skip: int
    limit: int