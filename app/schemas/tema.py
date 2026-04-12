from pydantic import BaseModel, Field, field_validator
from typing import Optional
from html import escape
import re


class TemaBase(BaseModel):
    """Schema base con validaciones comunes"""
    nombre: Optional[str] = Field(None, min_length=2, max_length=50)
    descripcion: Optional[str] = Field(None, max_length=200)
    nivel_dificultad: Optional[str] = Field(None, max_length=50)
    
    @field_validator('nombre')
    @classmethod
    def validar_nombre(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        # Solo letras, números, espacios, acentos y algunos caracteres especiales
        if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-\.\,]+$', v):
            raise ValueError('Solo se permiten letras, números, espacios, guiones, puntos y comas')
        
        # Prevenir XSS
        v = escape(v)
        
        if len(v) < 2:
            raise ValueError('El nombre debe tener al menos 2 caracteres')
        
        return v.title()
    
    @field_validator('descripcion')
    @classmethod
    def validar_descripcion(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        # Prevenir XSS
        v = escape(v)
        
        if len(v) > 200:
            raise ValueError('La descripción no puede exceder 200 caracteres')
        
        return v
    
    @field_validator('nivel_dificultad')
    @classmethod
    def validar_nivel_dificultad(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        
        v = v.strip().lower()
        
        niveles_validos = ['basico', 'básico', 'intermedio', 'avanzado', 'experto']
        
        if v not in niveles_validos:
            raise ValueError(
                f"Nivel de dificultad inválido. Valores permitidos: {', '.join(niveles_validos)}"
            )
        
        # Normalizar
        normalizacion = {
            'basico': 'básico',
            'básico': 'básico',
            'intermedio': 'intermedio',
            'avanzado': 'avanzado',
            'experto': 'experto'
        }
        
        return normalizacion.get(v, v)


class TemaCreate(BaseModel):
    """Schema para crear un tema"""
    nombre: str = Field(..., min_length=2, max_length=50)
    descripcion: Optional[str] = Field(None, max_length=200)
    nivel_dificultad: str = Field(..., max_length=50)
    
    @field_validator('nombre')
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-\.\,]+$', v):
            raise ValueError('Solo se permiten letras, números, espacios, guiones, puntos y comas')
        
        v = escape(v)
        
        if len(v) < 2:
            raise ValueError('El nombre debe tener al menos 2 caracteres')
        
        return v.title()
    
    @field_validator('descripcion')
    @classmethod
    def validar_descripcion(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        v = escape(v)
        
        return v
    
    @field_validator('nivel_dificultad')
    @classmethod
    def validar_nivel_dificultad(cls, v: str) -> str:
        v = v.strip().lower()
        
        niveles_validos = ['basico', 'básico', 'intermedio', 'avanzado', 'experto']
        
        if v not in niveles_validos:
            raise ValueError(
                f"Nivel de dificultad inválido. Valores permitidos: {', '.join(niveles_validos)}"
            )
        
        normalizacion = {
            'basico': 'básico',
            'básico': 'básico'
        }
        
        return normalizacion.get(v, v)


class TemaUpdate(BaseModel):
    """Schema para actualizar un tema"""
    nombre: Optional[str] = Field(None, min_length=2, max_length=50)
    descripcion: Optional[str] = Field(None, max_length=200)
    nivel_dificultad: Optional[str] = Field(None, max_length=50)
    
    @field_validator('nombre')
    @classmethod
    def validar_nombre(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        if not re.match(r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s\-\.\,]+$', v):
            raise ValueError('Solo se permiten letras, números, espacios, guiones, puntos y comas')
        
        v = escape(v)
        
        if len(v) < 2:
            raise ValueError('El nombre debe tener al menos 2 caracteres')
        
        return v.title()
    
    @field_validator('descripcion')
    @classmethod
    def validar_descripcion(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        v = escape(v)
        
        return v
    
    # @field_validator('nivel_dificultad')
    # @classmethod
    # def validar_nivel_dificultad(cls, v: Optional[str]) -> Optional[str]:
    #     if v is None:
    #         return v
        
    #     v = v.strip().lower()
        
    #     niveles_validos = ['basico', 'básico', 'intermedio', 'avanzado', 'experto']
        
    #     if v not in niveles_validos:
    #         raise ValueError(
    #             f"Nivel de dificultad inválido. Valores permitidos: {', '.join(niveles_validos)}"
    #         )
        
    #     normalizacion = {
    #         'basico': 'básico',
    #         'básico': 'básico'
    #     }
        
    #     return normalizacion.get(v, v)


class SubtemaSimple(BaseModel):
    id_subtema: int
    nombre: str
    
    class Config:
        from_attributes = True

class Tema(TemaBase):
    """Schema de respuesta"""
    id_tema: int
    subtemas: list[SubtemaSimple] = []
    
    class Config:
        from_attributes = True