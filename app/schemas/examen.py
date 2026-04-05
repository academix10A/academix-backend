from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
import re
from html import escape
from datetime import datetime


class ExamenBase(BaseModel):
    titulo: Optional[str] = Field(None, min_length=3, max_length=200)
    descripcion: Optional[str] = Field(None, min_length=10, max_length=1000)
    cantidad_preguntas: Optional[int] = Field(None, gt=0, le=100)
    id_subtema: Optional[int] = Field(None, gt=0)

    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        if len(v) < 3:
            raise ValueError('El título debe tener al menos 3 caracteres')
        if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-_.,;:()¿?¡!]+$', v):
            raise ValueError('El título contiene caracteres no permitidos')
        return escape(v)

    @field_validator('descripcion')
    @classmethod
    def sanitizar_descripcion(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        if len(v) < 10:
            raise ValueError('La descripción debe tener al menos 10 caracteres')
        if re.search(r'<script|<iframe|javascript:|onerror=|onclick=', v, re.IGNORECASE):
            raise ValueError('Contenido no permitido en la descripción')
        return escape(v)

class ExamenRealizadoDetalle(BaseModel):
    id_intento: int
    id_examen: int
    titulo_examen: str
    calificacion: float
    fecha: datetime
    respuestas_correctas: int
    cantidad_preguntas: int
    aprobo: bool
    porcentaje: float

    class Config:
        from_attributes = True

class ExamenCreate(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=200)
    descripcion: str = Field(..., min_length=10, max_length=1000)
    cantidad_preguntas: int = Field(..., gt=0, le=100)
    id_subtema: int = Field(..., gt=0)

    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v: str) -> str:
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        if len(v) < 3:
            raise ValueError('El título debe tener al menos 3 caracteres')
        if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-_.,;:()¿?¡!]+$', v):
            raise ValueError('El título contiene caracteres no permitidos')
        return escape(v)

    @field_validator('descripcion')
    @classmethod
    def sanitizar_descripcion(cls, v: str) -> str:
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        if len(v) < 10:
            raise ValueError('La descripción debe tener al menos 10 caracteres')
        if re.search(r'<script|<iframe|javascript:|onerror=|onclick=', v, re.IGNORECASE):
            raise ValueError('Contenido no permitido en la descripción')
        return escape(v)


class ExamenUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=3, max_length=200)
    descripcion: Optional[str] = Field(None, min_length=10, max_length=1000)
    cantidad_preguntas: Optional[int] = Field(None, gt=0, le=100)
    id_subtema: Optional[int] = Field(None, gt=0)

    @field_validator('titulo')
    @classmethod
    def sanitizar_titulo(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        if len(v) < 3:
            raise ValueError('El título debe tener al menos 3 caracteres')
        if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-_.,;:()¿?¡!]+$', v):
            raise ValueError('El título contiene caracteres no permitidos')
        return escape(v)

    @field_validator('descripcion')
    @classmethod
    def sanitizar_descripcion(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        if len(v) < 10:
            raise ValueError('La descripción debe tener al menos 10 caracteres')
        if re.search(r'<script|<iframe|javascript:|onerror=|onclick=', v, re.IGNORECASE):
            raise ValueError('Contenido no permitido en la descripción')
        return escape(v)


# Schema público de opción (SIN es_correcta)
class OpcionPublica(BaseModel):
    id_opcion: int
    respuesta: str

    class Config:
        from_attributes = True


# Schema público de opción con resultado (DESPUÉS de responder)
class OpcionResultado(BaseModel):
    id_opcion: int
    respuesta: str
    es_correcta: bool

    class Config:
        from_attributes = True


# Pregunta con sus opciones públicas
class PreguntaConOpciones(BaseModel):
    id_pregunta: int
    contenido: str
    opciones: List[OpcionPublica]

    class Config:
        from_attributes = True


# Examen completo (para tomar el examen)
class ExamenCompleto(BaseModel):
    id_examen: int
    titulo: str
    descripcion: str
    cantidad_preguntas: int
    id_subtema: int
    preguntas: List[PreguntaConOpciones]

    class Config:
        from_attributes = True


# Lo que el frontend envía al terminar el examen
class RespuestaUsuario(BaseModel):
    id_pregunta: int
    id_opcion: int


class ExamenSubmit(BaseModel):
    id_examen: int
    id_usuario: int
    respuestas: List[RespuestaUsuario]


class ExamenRealizado(BaseModel):
    id_intento: int
    id_examen: int
    titulo_examen: str
    calificacion: float
    fecha: datetime

    class Config:
        from_attributes = True


# Detalle de una pregunta en el resultado
class PreguntaResultado(BaseModel):
    id_pregunta: int
    contenido: str
    id_opcion_elegida: int
    respuesta_elegida: str
    es_correcta: bool
    opciones: List[OpcionResultado]


# Resultado completo del examen
class ExamenResultado(BaseModel):
    id_intento: int
    id_examen: int
    titulo_examen: str
    calificacion: float
    correctas: int
    total: int
    porcentaje: float
    preguntas: List[PreguntaResultado]


# ── Schema principal de Examen (el que usa GET /examen/) ──────────────────────
# Incluye nombre_subtema para que Flutter pueda filtrar por subtema sin
# hacer llamadas extra al backend.
class SubtemaBasico(BaseModel):
    """Datos mínimos del subtema embebidos en la respuesta de Examen."""
    id_subtema: int
    nombre: str
    nivel_dificultad: Optional[str] = None

    class Config:
        from_attributes = True


class Examen(ExamenBase):
    id_examen: int
    # Subtema anidado — Flutter lee subtema["nombre"] para los chips de filtro
    subtema: Optional[SubtemaBasico] = None

    class Config:
        from_attributes = True