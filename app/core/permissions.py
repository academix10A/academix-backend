from app.models.usuario import Usuario



def is_admin(user: Usuario) -> bool:
    """
    Verifica si un usuario es administrador.
    Versión ROBUSTA - Maneja casos edge.
    """
    # Paso 1: ¿El usuario existe?
    if not user:
        return False
    
    # Paso 2: ¿El usuario tiene un rol asignado?
    if not user.rol:
        return False
    
    # Paso 3: ¿El rol tiene un nombre?
    if not user.rol.nombre:
        return False
    
    # Paso 4: Comparar (insensible a mayúsculas/minúsculas)
    return user.rol.nombre.lower() == "administrador"


def has_role(user: Usuario, role_name: str) -> bool:
    """
    Verifica si un usuario tiene un rol específico.
    FLEXIBLE - Funciona con cualquier rol.
    
    Ejemplo:
        has_role(user, "administrador")  → True/False
        has_role(user, "estudiante")     → True/False
        has_role(user, "usuario")        → True/False
    """
    # Mismas validaciones que is_admin
    if not user:
        return False
    
    if not user.rol:
        return False
    
    if not user.rol.nombre:
        return False
    
    # Comparar con el rol que le pasemos
    return user.rol.nombre.lower() == role_name.lower()