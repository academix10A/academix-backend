from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.estado import Estado
from app.schemas.estado import EstadoCreate, EstadoUpdate


def get_estado(db: Session, estado_id: int) -> Optional[Estado]:
    """Obtiene un estado por su ID."""
    return db.query(Estado).filter(Estado.id_estado == estado_id).first()


def get_estado_by_nombre(db: Session, nombre: str) -> Optional[Estado]:
    """Obtiene un estado por su nombre."""
    return db.query(Estado).filter(Estado.nombre == nombre).first()


def get_estados(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Estado]:
    """Obtiene una lista de estado con paginación."""
    return db.query(Estado).offset(skip).limit(limit).all()

def create_estado(db: Session, estado_in: EstadoCreate) -> Estado:
    """Crea un estado nuevo."""
    db_obj = Estado(
        nombre=estado_in.nombre
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_estado(
    db: Session, 
    estado_id: int, 
    estado_in: EstadoUpdate
) -> Optional[Estado]:
    """Actualiza un tema existente."""
    db_obj = get_estado(db, estado_id=estado_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = estado_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_estado(db: Session, estado_id: int) -> Optional[Estado]:
    """Elimina un estado por su ID."""
    db_obj = get_estado(db, estado_id=estado_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_estados(db: Session) -> int:
    """Cuenta el total de temas en la base de datos."""
    return db.query(Estado).count()