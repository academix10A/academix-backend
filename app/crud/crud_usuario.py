from typing import Optional, List

from sqlalchemy.orm import Session
from app.core.security import get_password_hash
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate


def get_usuario(db: Session, usuario_id: int) -> Optional[Usuario]:
    """Obtiene un usuario por su ID."""
    return db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()


def get_usuario_by_nombre(db: Session, nombre: str) -> Optional[Usuario]:
    """Obtiene un usuario por su nombre."""
    return db.query(Usuario).filter(Usuario.nombre == nombre).first()


def get_usuario_by_correo(db: Session, correo: str) -> Optional[Usuario]:
    """Obtiene un usuario por su correo."""
    return db.query(Usuario).filter(Usuario.correo == correo).first()


def get_usuarios(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Usuario]:
    """Obtiene una lista de usuarios con paginación."""
    return db.query(Usuario).offset(skip).limit(limit).all()


def create_usuario(db: Session, usuario_in: UsuarioCreate) -> Usuario:
    """Crea un usuario nuevo."""
    db_obj = Usuario(
        nombre=usuario_in.nombre,
        apellido_paterno=usuario_in.apellido_paterno,
        apellido_materno=usuario_in.apellido_materno,
        correo=usuario_in.correo,
        contrasena_hash=get_password_hash(usuario_in.contrasena),
        id_rol=usuario_in.id_rol,
        estado=usuario_in.estado or "activo"  # Por defecto activo
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_usuario(
    db: Session, 
    usuario_id: int, 
    usuario_in: UsuarioUpdate
) -> Optional[Usuario]:
    """Actualiza un usuario existente."""
    db_obj = get_usuario(db, usuario_id=usuario_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = usuario_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_usuario(db: Session, usuario_id: int) -> Optional[Usuario]:
    """Elimina un usuario por su ID."""
    db_obj = get_usuario(db, usuario_id=usuario_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_usuario(db: Session) -> int:
    """Cuenta el total de usuarios en la base de datos."""
    return db.query(Usuario).count()


def is_active(user: Usuario) -> bool:
    """Verifica si un usuario está activo."""
    return user.estado == "activo"


def authenticate(db: Session, correo: str, password: str) -> Optional[Usuario]:
    """Autentica un usuario por correo y contraseña."""
    from app.core.security import verify_password
    
    user = get_usuario_by_correo(db, correo=correo)
    if not user:
        return None
    if not verify_password(password, user.contrasena_hash):
        return None
    return user