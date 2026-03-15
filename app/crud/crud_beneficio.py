from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.beneficio import Beneficio
from app.schemas.beneficio import BeneficioCreate, BeneficioUpdate


def get_beneficio(db: Session, beneficio_id: int) -> Optional[Beneficio]:
    """Obtiene un beneficio por su ID."""
    return db.query(Beneficio).filter(Beneficio.id_beneficio == beneficio_id).first()


def get_beneficio_by_nombre(db: Session, nombre: str) -> Optional[Beneficio]:
    """Obtiene un beneficio por su nombre."""
    return db.query(Beneficio).filter(Beneficio.nombre == nombre).first()


def get_beneficios(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Beneficio]:
    """Obtiene una lista de beneficios con paginación."""
    return db.query(Beneficio).offset(skip).limit(limit).all()

def create_beneficio(db: Session, beneficio_in: BeneficioCreate) -> Beneficio:
    """Crea un beneficio nuevo."""
    db_obj = Beneficio(
        nombre=beneficio_in.nombre,
        descripcion=beneficio_in.descripcion
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_beneficio(
    db: Session, 
    beneficio_id: int, 
    beneficio_in: BeneficioUpdate
) -> Optional[Beneficio]:
    """Actualiza un beneficio existente."""
    db_obj = get_beneficio(db, beneficio_id=beneficio_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = beneficio_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_beneficio(db: Session, beneficio_id: int) -> Optional[Beneficio]:
    """Elimina un beneficio por su ID."""
    db_obj = get_beneficio(db, beneficio_id=beneficio_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_beneficio(db: Session) -> int:
    """Cuenta el total de beneficios en la base de datos."""
    return db.query(Beneficio).count()