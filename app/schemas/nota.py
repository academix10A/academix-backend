# app/schemas/nota.py
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime
import re
from html import escape

# ── Validador reutilizable ────────────────────────────────────────────────────
_PATRONES_PELIGROSOS = [
    r'<script', r'</script>', r'<iframe', r'</iframe>',
    r'<object', r'</object>', r'<embed', r'</embed>',
    r'javascript:', r'onerror\s*=', r'onclick\s*=', r'onload\s*=',
    r'onmouseover\s*=', r'onmouseenter\s*=', r'onfocus\s*=', r'onblur\s*=',
    r'<link.*stylesheet', r'@import', r'vbscript:', r'data:text/html',
    r'<style', r'</style>', r'<form', r'</form>',
]

def _sanitizar(v: str) -> str:
    """Limpia y valida el contenido. Lanza ValueError si hay contenido malicioso."""
    v = v.strip()
    v = re.sub(r' +', ' ', v)
    v = re.sub(r'\n\s*\n\s*\n\s*\n+', '\n\n\n', v)

    if len(v) < 1:
        raise ValueError('El contenido no puede estar vacío')

    for patron in _PATRONES_PELIGROSOS:
        if re.search(patron, v, re.IGNORECASE):
            raise ValueError('Contenido no permitido detectado en la nota')

    return escape(v)


# ── Schemas ───────────────────────────────────────────────────────────────────

class UsuarioNota(BaseModel):
    id_usuario: int
    nombre: str
    apellido_paterno: str

    class Config:
        from_attributes = True

class NotaBase(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=25)
    contenido:    Optional[str]  = Field(None, min_length=1, max_length=5000)
    es_compartida: Optional[bool] = None
    id_usuario:   Optional[int]  = Field(None, gt=0)
    id_recurso:   Optional[int]  = Field(None, gt=0)
    
    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        if len(v) < 1:
            raise ValueError("El título no puede estar vacío")
        return escape(v)

    @field_validator('contenido')
    @classmethod
    def sanitizar_contenido(cls, v: Optional[str]) -> Optional[str]:
        return _sanitizar(v) if v is not None else v

class NotaCompartidaResponse(BaseModel):
    id_nota: int
    titulo: str
    contenido: str
    fecha_creacion: datetime

    usuario: Optional[UsuarioNota] = None

    class Config:
        from_attributes = True


class NotasPorRecursoResponse(BaseModel):
    id_recurso: int
    notas: List[NotaCompartidaResponse]

class NotaCreate(BaseModel):
    """
    Schema de creación.
    Nota: id_usuario se acepta en el body pero el endpoint lo sobreescribe
    con el id del token JWT — nunca se usa el valor que manda el cliente.
    """
    titulo: str = Field(..., min_length=1, max_length=25)
    contenido:     str  = Field(..., min_length=1, max_length=5000)
    es_compartida: bool = Field(..., description="Si la nota es visible para otros usuarios")
    id_recurso:    int  = Field(..., gt=0)
    
    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        if len(v) < 1:
            raise ValueError("El título no puede estar vacío")
        return escape(v)

    @field_validator('contenido')
    @classmethod
    def sanitizar_contenido(cls, v: str) -> str:
        return _sanitizar(v)


class NotaUpdate(BaseModel):
    """Solo contenido y es_compartida son editables por el usuario."""
    titulo: Optional[str] = Field(None, min_length=1, max_length=25)
    contenido:     Optional[str]  = Field(None, min_length=1, max_length=5000)
    es_compartida: Optional[bool] = None
    # id_usuario e id_recurso NO están aquí a propósito —
    # no se permite cambiar a quién pertenece una nota ni su recurso.
    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        if len(v) < 1:
            raise ValueError("El título no puede estar vacío")
        return escape(v)

    @field_validator('contenido')
    @classmethod
    def sanitizar_contenido(cls, v: Optional[str]) -> Optional[str]:
        return _sanitizar(v) if v is not None else v


class Nota(NotaBase):
    id_nota: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime

    usuario: Optional[UsuarioNota] = None

    class Config:
        from_attributes = True