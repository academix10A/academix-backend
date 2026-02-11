from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.rol import Rol
from app.schemas.rol import RolCreate, RolUpdate


def get_rol(db: Session, rol_id: int) -> Optional[Rol]:
    """Obtiene un rol por su ID."""
    return db.query(Rol).filter(Rol.id_rol == rol_id).first()


def get_rol_by_nombre(db: Session, nombre: str) -> Optional[Rol]:
    """Obtiene un rol por su nombre."""
    return db.query(Rol).filter(Rol.nombre == nombre).first()


def get_roles(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Rol]:
    """Obtiene una lista de roles con paginación."""
    return db.query(Rol).offset(skip).limit(limit).all()

def create_rol(db: Session, rol_in: RolCreate) -> Rol:
    """Crea un rol nuevo."""
    db_obj = Rol(
        nombre=rol_in.nombre
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_rol(
    db: Session, 
    rol_id: int, 
    rol_in: RolUpdate
) -> Optional[Rol]:
    """Actualiza un rol existente."""
    db_obj = get_rol(db, rol_id=rol_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = rol_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_rol(db: Session, rol_id: int) -> Optional[Rol]:
    """Elimina un rol por su ID."""
    db_obj = get_rol(db, rol_id=rol_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_rol(db: Session) -> int:
    """Cuenta el total de rol en la base de datos."""
    return db.query(Rol).count()