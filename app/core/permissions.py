from typing import List, Optional
from fastapi import Depends, HTTPException, status
from app.api.deps import get_current_active_user
from app.models.usuario import Usuario


class PermissionChecker:
    """
    Verificador de permisos basado en roles y membresías.
    Se instancia con los permisos requeridos y se usa como dependencia en los endpoints.
    
    Uso:
        Depends(PermissionChecker(roles=["admin"]))
        Depends(PermissionChecker(membresias=["premium", "gratis"]))
        Depends(PermissionChecker(roles=["admin"], membresias=["premium"]))
    """
    
    def __init__(
        self, 
        roles: Optional[List[str]] = None, 
        membresias: Optional[List[str]] = None
    ):
        self.roles = [r.lower() for r in roles] if roles else []
        self.membresias = [m.lower() for m in membresias] if membresias else []
    
    def __call__(
        self, 
        current_user: Usuario = Depends(get_current_active_user)
    ) -> Usuario:
        
        # Extraer rol y membresía del usuario
        user_rol = current_user.rol.nombre.lower() if current_user.rol else None
        print(current_user.membresias)
        for m in current_user.membresias:
            print(m.__dict__)
        # user_membresia = current_user.membresias.nombre.lower() if current_user.membresias else None
        user_membresias = [
            m.membresia.nombre.lower()
            for m in current_user.membresias
            if m.membresia and m.activa
        ]
        
        # Admin siempre pasa — es el superusuario
        if user_rol == "admin":
            return current_user
        
        # Verificar rol
        if self.roles and user_rol in self.roles:
            return current_user
        
        # Verificar membresía
        # if self.membresias and user_membresia in self.membresias:
        #     return current_user
        if self.membresias and any(m in self.membresias for m in user_membresias):
            return current_user
        
        # Si no cumple ninguna condición
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos suficientes para realizar esta acción"
        )