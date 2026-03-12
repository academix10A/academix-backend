from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.etiqueta import Etiqueta
from app.schemas.etiqueta import EtiquetaCreate, EtiquetaUpdate


def get_etiqueta(db: Session, etiqueta_id: int) -> Optional[Etiqueta]:
    """Obtiene un etiqueta por su ID."""
    return db.query(Etiqueta).filter(Etiqueta.id_etiqueta == etiqueta_id).first()


def get_etiqueta_by_nombre(db: Session, nombre: str) -> Optional[Etiqueta]:
    """Obtiene una etiqueta por su nombre."""
    return db.query(Etiqueta).filter(Etiqueta.nombre == nombre).first()


def get_etiquetas(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Etiqueta]:
    """Obtiene una lista de etiquetas con paginación."""
    return db.query(Etiqueta).offset(skip).limit(limit).all()

def create_etiqueta(db: Session, etiqueta_in: EtiquetaCreate) -> Etiqueta:
    """Crea un etiqueta nuevo."""
    db_obj = Etiqueta(
        nombre=etiqueta_in.nombre
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_etiqueta(
    db: Session, 
    etiqueta_id: int, 
    etiqueta_in: EtiquetaUpdate
) -> Optional[Etiqueta]:
    """Actualiza un rol existente."""
    db_obj = get_etiqueta(db, etiqueta_id=etiqueta_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = etiqueta_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_etiqueta(db: Session, etiqueta_id: int) -> Optional[Etiqueta]:
    """Elimina un etiqueta por su ID."""
    db_obj = get_etiqueta(db, etiqueta_id=etiqueta_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_etiqueta(db: Session) -> int:
    """Cuenta el total de rol en la base de datos."""
    return db.query(Etiqueta).count()