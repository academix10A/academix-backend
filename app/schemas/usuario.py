from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import Optional
from datetime import datetime
import re
from html import escape


class UsuarioBase(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=150)
    apellido_paterno: Optional[str] = Field(None, min_length=2, max_length=150)
    apellido_materno: Optional[str] = Field(None, min_length=2, max_length=150)
    correo: Optional[EmailStr] = None
    id_estado: Optional[int] = Field(None, gt=0, description="ID del estado debe ser positivo")
    id_rol: Optional[int] = Field(None, gt=0, description="ID del rol debe ser positivo")
    id_membresia: Optional[int] = Field(None, gt=0, description="ID de la membresia debe ser positivo")
    
    @field_validator('nombre', 'apellido_paterno', 'apellido_materno')
    @classmethod
    def sanitizar_nombres(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza nombres: elimina caracteres peligrosos y espacios extras"""
        if v is None:
            return v
        
        # Eliminar espacios al inicio y final
        v = v.strip()
        
        # Eliminar múltiples espacios
        v = re.sub(r'\s+', ' ', v)
        
        # Solo permitir letras, espacios, acentos y guiones
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\-]+$', v):
            raise ValueError('Solo se permiten letras, espacios y guiones en los nombres')
        
        # Escapar HTML para prevenir XSS (aunque no deberías renderizar esto en HTML sin escapar)
        v = escape(v)
        
        return v.title()  # Capitalizar cada palabra
    
    @field_validator('correo')
    @classmethod
    def validar_correo(cls, v: Optional[EmailStr]) -> Optional[EmailStr]:
        """Validaciones adicionales de correo"""
        if v is None:
            return v
        
        # Convertir a minúsculas
        v = v.lower().strip()
        
        # Validar longitud total
        if len(v) > 150:
            raise ValueError('El correo es demasiado largo')
        
        # Validar dominios sospechosos (opcional - personaliza según tu caso)
        dominios_bloqueados = ['tempmail.com', 'guerrillamail.com', '10minutemail.com']
        dominio = v.split('@')[1] if '@' in v else ''
        if dominio in dominios_bloqueados:
            raise ValueError('Dominio de correo no permitido')
        
        return v


class UsuarioCreate(BaseModel):

    nombre: str = Field(..., min_length=2, max_length=150, description="Nombre del usuario")
    apellido_paterno: str = Field(..., min_length=2, max_length=150, description="Apellido paterno")
    apellido_materno: str = Field(..., min_length=2, max_length=150, description="Apellido materno")
    correo: EmailStr = Field(..., description="Correo electrónico válido")
    contrasena: str = Field(..., min_length=8, max_length=128, description="Contraseña (mínimo 8 caracteres)")
    id_rol: int = Field(..., gt=0, description="ID del rol (debe existir)")
    id_estado: int = Field(..., gt=0, description="ID del estado (debe existir)")
    id_membresia: int = Field(..., gt=0, description="ID de la membresia (debe existir)")
    
    @field_validator('nombre', 'apellido_paterno', 'apellido_materno')
    @classmethod
    def sanitizar_nombres(cls, v: str) -> str:
        """Sanitiza y valida nombres"""
        # Eliminar espacios
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        # Solo letras, espacios, acentos y guiones
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\-]+$', v):
            raise ValueError('Solo se permiten letras, espacios y guiones en los nombres')
        
        # Prevenir XSS
        v = escape(v)
        
        # Validar longitud mínima después de limpiar
        if len(v) < 2:
            raise ValueError('El nombre debe tener al menos 2 caracteres')
        
        return v.title()
    
    @field_validator('correo')
    @classmethod
    def validar_correo(cls, v: EmailStr) -> EmailStr:
        """Validaciones adicionales de correo"""
        v = v.lower().strip()
        
        if len(v) > 150:
            raise ValueError('El correo es demasiado largo (máximo 150 caracteres)')
        
        # Validar que tenga formato válido adicional
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', v):
            raise ValueError('Formato de correo inválido')
        
        return v
    
    @field_validator('contrasena')
    @classmethod
    def validar_contrasena(cls, v: str) -> str:
        """
        Validación ROBUSTA de contraseña:
        - Mínimo 8 caracteres
        - Al menos 1 mayúscula
        - Al menos 1 minúscula
        - Al menos 1 número
        - Al menos 1 carácter especial
        """
        if len(v) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres')
        
        if len(v) > 128:
            raise ValueError('La contraseña es demasiado larga (máximo 128 caracteres)')
        
        # Validar complejidad
        tiene_mayuscula = bool(re.search(r'[A-Z]', v))
        tiene_minuscula = bool(re.search(r'[a-z]', v))
        tiene_numero = bool(re.search(r'\d', v))
        tiene_especial = bool(re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=\[\]\\\/~`]', v))
        
        errores = []
        if not tiene_mayuscula:
            errores.append('al menos 1 mayúscula')
        if not tiene_minuscula:
            errores.append('al menos 1 minúscula')
        if not tiene_numero:
            errores.append('al menos 1 número')
        if not tiene_especial:
            errores.append('al menos 1 carácter especial (!@#$%^&*...)')
        
        if errores:
            raise ValueError(f"La contraseña debe contener: {', '.join(errores)}")
        
        # Validar contraseñas comunes (top 100)
        contraseñas_comunes = {
            'password', 'password123', '12345678', 'qwerty123', 'abc123456',
            'password1', 'Passw0rd', 'Welcome1', 'Admin123', 'letmein1'
        }
        if v.lower() in contraseñas_comunes:
            raise ValueError('Contraseña demasiado común, elige una más segura')
        
        return v
    
    @model_validator(mode='after')
    def validar_datos_completos(self):
        """Validación a nivel de modelo completo"""
        # Verificar que el correo no contenga el nombre (para evitar correos débiles)
        nombre_lower = self.nombre.lower()
        correo_lower = self.correo.lower()
        
        # Esto es opcional, pero es una buena práctica
        if nombre_lower in correo_lower and len(nombre_lower) > 3:
            # Esto es solo una advertencia, no bloquea
            pass
        
        return self


class UsuarioUpdate(BaseModel):
    
    nombre: Optional[str] = Field(None, min_length=2, max_length=150)
    apellido_paterno: Optional[str] = Field(None, min_length=2, max_length=150)
    apellido_materno: Optional[str] = Field(None, min_length=2, max_length=150)
    correo: Optional[EmailStr] = None
    id_estado: Optional[int] = Field(None, gt=0)
    id_rol: Optional[int] = Field(None, gt=0)
    id_membresia: Optional[int] = Field(None, gt=0)
    contrasena: Optional[str] = Field(None, min_length=8, max_length=128)
    
    @field_validator('nombre', 'apellido_paterno', 'apellido_materno')
    @classmethod
    def sanitizar_nombres(cls, v: Optional[str]) -> Optional[str]:
        """Sanitiza nombres si están presentes"""
        if v is None:
            return v
        
        v = v.strip()
        v = re.sub(r'\s+', ' ', v)
        
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\-]+$', v):
            raise ValueError('Solo se permiten letras, espacios y guiones en los nombres')
        
        v = escape(v)
        
        if len(v) < 2:
            raise ValueError('El nombre debe tener al menos 2 caracteres')
        
        return v.title()
    
    @field_validator('correo')
    @classmethod
    def validar_correo(cls, v: Optional[EmailStr]) -> Optional[EmailStr]:
        """Validar correo si está presente"""
        if v is None:
            return v
        
        v = v.lower().strip()
        
        if len(v) > 150:
            raise ValueError('El correo es demasiado largo')
        
        return v
    
    @field_validator('contrasena')
    @classmethod
    def validar_contrasena(cls, v: Optional[str]) -> Optional[str]:
        """Validar contraseña si se está actualizando"""
        if v is None:
            return v
        
        # Mismas validaciones que en Create
        if len(v) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres')
        
        if len(v) > 128:
            raise ValueError('La contraseña es demasiado larga')
        
        tiene_mayuscula = bool(re.search(r'[A-Z]', v))
        tiene_minuscula = bool(re.search(r'[a-z]', v))
        tiene_numero = bool(re.search(r'\d', v))
        tiene_especial = bool(re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=\[\]\\\/~`]', v))
        
        errores = []
        if not tiene_mayuscula:
            errores.append('al menos 1 mayúscula')
        if not tiene_minuscula:
            errores.append('al menos 1 minúscula')
        if not tiene_numero:
            errores.append('al menos 1 número')
        if not tiene_especial:
            errores.append('al menos 1 carácter especial')
        
        if errores:
            raise ValueError(f"La contraseña debe contener: {', '.join(errores)}")
        
        return v


class Usuario(UsuarioBase):
    """Schema de respuesta - Lo que se devuelve al cliente"""
    
    id_usuario: int
    contrasena_hash: str 
    fecha_registro: datetime
    
    class Config:
        from_attributes = True


class UsuarioPublico(BaseModel):
    """Schema PÚBLICO - Sin información sensible"""
    
    id_usuario: int
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    correo: EmailStr
    id_estado: int
    id_rol: int
    id_membresia: int
    fecha_registro: datetime
    
    class Config:
        from_attributes = True


class UsuarioConRol(UsuarioPublico):
    """Schema con información del rol"""
    
    nombre_rol: Optional[str] = None  
    
    class Config:
        from_attributes = True
