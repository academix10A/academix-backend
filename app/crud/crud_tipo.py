from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.tipo import Tipo
from app.schemas.tipo import TipoCreate, TipoUpdate


def get_tipo(db: Session, tipo_id: int) -> Optional[Tipo]:
    """Obtiene un rol por su ID."""
    return db.query(Tipo).filter(Tipo.id_tipo == tipo_id).first()


def get_tipo_by_nombre(db: Session, nombre: str) -> Optional[Tipo]:
    """Obtiene un tipo por su nombre."""
    return db.query(Tipo).filter(Tipo.nombre == nombre).first()


def get_tipos(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Tipo]:
    """Obtiene una lista de tipos con paginación."""
    return db.query(Tipo).offset(skip).limit(limit).all()

def create_tipo(db: Session, tipo_in: TipoCreate) -> Tipo:
    """Crea un tipo nuevo."""
    db_obj = Tipo(
        nombre=tipo_in.nombre
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_tipo(
    db: Session, 
    tipo_id: int, 
    tipo_in: TipoUpdate
) -> Optional[Tipo]:
    """Actualiza un tipo existente."""
    db_obj = get_tipo(db, tipo_id=tipo_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = tipo_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_tipo(db: Session, tipo_id: int) -> Optional[Tipo]:
    """Elimina un tipo por su ID."""
    db_obj = get_tipo(db, tipo_id=tipo_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_tipo(db: Session) -> int:
    """Cuenta el total de tipos en la base de datos."""
    return db.query(Tipo).count()