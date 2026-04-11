from typing import List, Optional
from fastapi import Depends, HTTPException, status
from app.api.deps import get_current_active_user
from app.models.usuario import Usuario
import unicodedata


def normalize(text: str) -> str:
    text = text.strip().lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return text


def has_benefit(user: Usuario, benefit: str) -> bool:
    """
    Helper para verificar si un usuario tiene un beneficio específico.
    Útil para lógica condicional dentro de endpoints (ej: intentos, resultados).

    Uso:
        if has_benefit(current_user, Beneficios.INTENTOS_ILIMITADOS):
            pass  # no hay límite
    """
    benefit_normalized = normalize(benefit)
    for m in user.membresias:
        if m.membresia and m.activa:
            for b in m.membresia.beneficios:
                if b.nombre and normalize(b.nombre) == benefit_normalized:
                    return True
    return False


def is_admin(user: Usuario) -> bool:
    return bool(
        user.rol and
        user.rol.nombre and
        user.rol.nombre.lower() == "admin"
    )


class PermissionChecker:
    """
    Verificador de permisos basado en:
    - Roles
    - Membresías
    - Beneficios

    Uso:
        Depends(PermissionChecker(roles=["admin"]))
        Depends(PermissionChecker(membresias=["plan premium mensual"]))
        Depends(PermissionChecker(beneficios=[Beneficios.IA]))
        Depends(PermissionChecker(beneficios=[Beneficios.EXAMENES_AVANZADOS, Beneficios.DESGLOSE], require_all_benefits=True))
    """

    def __init__(
        self,
        roles: Optional[List[str]] = None,
        membresias: Optional[List[str]] = None,
        beneficios: Optional[List[str]] = None,
        require_all_benefits: bool = False
    ):
        self.roles = [r.lower() for r in roles] if roles else []
        self.membresias = [m.lower() for m in membresias] if membresias else []
        self.beneficios = [normalize(b) for b in beneficios] if beneficios else []
        self.require_all_benefits = require_all_benefits

    def __call__(
        self,
        current_user: Usuario = Depends(get_current_active_user)
    ) -> Usuario:

        user_rol = current_user.rol.nombre.lower() if current_user.rol else None

        user_membresias = [
            m.membresia.nombre.lower()
            for m in current_user.membresias
            if m.membresia and m.activa
        ]

        user_beneficios = []
        for m in current_user.membresias:
            if m.membresia and m.activa:
                for b in m.membresia.beneficios:
                    if b.nombre:
                        user_beneficios.append(normalize(b.nombre))

        # Admin bypass
        if user_rol == "admin":
            return current_user

        # Verificar rol
        if self.roles:
            if user_rol in self.roles:
                return current_user

        # Verificar membresía
        if self.membresias:
            if any(m in self.membresias for m in user_membresias):
                return current_user

        # Verificar beneficios
        if self.beneficios:
            if self.require_all_benefits:
                if all(b in user_beneficios for b in self.beneficios):
                    return current_user
            else:
                if any(b in user_beneficios for b in self.beneficios):
                    return current_user

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos suficientes para realizar esta acción"
        )


class Beneficios:
    # Contenido
    BIBLIOTECA          = "acceso a biblioteca virtual"
    BUSQUEDA            = "busqueda y filtros avanzados"

    # Notas
    NOTAS               = "gestion de notas personales"
    NOTAS_COMPARTIDAS   = "publicacion de notas compartidas"

    # Exámenes — acceso
    EXAMENES_BASICOS    = "examenes por tema"
    EXAMENES_AVANZADOS  = "examenes por tema"

    # Exámenes — intentos
    INTENTOS_LIMITADOS  = "examenes por tema"
    INTENTOS_ILIMITADOS = "acceso premium completo"

    # Exámenes — resultados
    SOLO_CALIFICACION   = "examenes por tema"
    DESGLOSE            = "acceso premium completo"

    # Historial
    HISTORIAL           = "acceso premium completo"
    HISTORIAL_IA        = "historial de consultas ia"

    # Extras
    DESCARGA            = "descarga para uso offline"
    MODO_OFFLINE        = "acceso a funcionamiento offline"
    IA                  = "asistencia inteligente contextual"