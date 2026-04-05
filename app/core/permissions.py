from typing import List, Optional
from fastapi import Depends, HTTPException, status
from app.api.deps import get_current_active_user
from app.models.usuario import Usuario


def normalize(text: str) -> str:
    return text.strip().lower()


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
    BIBLIOTECA          = "acceso a biblioteca"
    BUSQUEDA            = "busqueda de recursos"

    # Notas
    NOTAS               = "gestion de notas"
    NOTAS_COMPARTIDAS   = "notas compartidas"

    # Exámenes — acceso
    EXAMENES_BASICOS    = "acceso a examenes basicos"
    EXAMENES_AVANZADOS  = "acceso a examenes avanzados"

    # Exámenes — intentos
    INTENTOS_LIMITADOS  = "intentos limitados (2 por examen)"
    INTENTOS_ILIMITADOS = "intentos ilimitados"

    # Exámenes — resultados
    SOLO_CALIFICACION   = "ver solo calificacion"
    DESGLOSE            = "ver desglose completo"

    # Historial
    HISTORIAL           = "historial de intentos"
    HISTORIAL_IA        = "historial ia"

    # Extras
    DESCARGA            = "descarga offline"
    MODO_OFFLINE        = "modo offline"
    IA                  = "asistente ia"