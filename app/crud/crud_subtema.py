from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.subtema import Subtema
from app.schemas.subtema import SubtemaCreate, SubtemaUpdate


def get_subtema(db: Session, subtema_id: int) -> Optional[Subtema]:
    """Obtiene un subtema por su ID."""
    return db.query(Subtema).filter(Subtema.id_subtema == subtema_id).first()


def get_subtema_by_nombre(db: Session, nombre: str) -> Optional[Subtema]:
    """Obtiene un subtema por su nombre."""
    return db.query(Subtema).filter(Subtema.nombre == nombre).first()


def get_subtemas(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Subtema]:
    """Obtiene una lista de subtemas con paginación."""
    return db.query(Subtema).offset(skip).limit(limit).all()


def get_subtemas_by_dificultad(
    db: Session, 
    nivel_dificultad: str
) -> List[Subtema]:
    """Obtiene subtemas filtrados por nivel de dificultad."""
    return db.query(Subtema).filter(
        Subtema.nivel_dificultad == nivel_dificultad
    ).all()


def create_subtema(db: Session, subtema_in: SubtemaCreate) -> Subtema:
    """Crea un Subtema nuevo."""
    db_obj = Subtema(
        nombre=subtema_in.nombre,
        descripcion=subtema_in.descripcion,
        nivel_dificultad=subtema_in.nivel_dificultad
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_subtema(
    db: Session, 
    subtema_id: int, 
    subtema_in: SubtemaUpdate
) -> Optional[Subtema]:
    """Actualiza un subtema existente."""
    db_obj = get_subtema(db, subtema_id=subtema_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = subtema_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_subtema(db: Session, subtema_id: int) -> Optional[Subtema]:
    """Elimina un subtema por su ID."""
    db_obj = get_subtema(db, subtema_id=subtema_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_subtemas(db: Session) -> int:
    """Cuenta el total de subtemas en la base de datos."""
    return db.query(Subtema).count()