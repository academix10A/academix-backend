from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.intento import Intento
from app.schemas.intento import IntentoCreate, IntentoUpdate


def get_intento(db: Session, intento_id: int) -> Optional[Intento]:
    """Obtiene un intento por su ID."""
    return db.query(Intento).filter(Intento.id_intento == intento_id).first()

def get_intentos(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Intento]:
    """Obtiene una lista de Intentos con paginación."""
    return db.query(Intento).offset(skip).limit(limit).all()


def get_intentos_usuario(
    db: Session, 
    id_usuario: int,
    skip: int = 0, 
    limit: int = 20
) -> List[Intento]:
    """Obtiene todos los intentos de un usuario específico."""
    return db.query(Intento).filter(
        Intento.id_usuario == id_usuario
    ).order_by(Intento.fecha.desc()).offset(skip).limit(limit).all()


def get_intento_by_calificacion(db: Session, calificacion: str) -> Optional[Intento]:
    """Obtiene un intento por su calificacion."""
    return db.query(Intento).filter(Intento.calificacion == calificacion).first()

def get_intento_by_user_and_exam(db: Session, id_usuario: int, id_examen: int):
    return db.query(Intento).filter(
        Intento.id_usuario == id_usuario, 
        Intento.id_examen == id_examen
    ).first()

def create_intento(db: Session, intento_in: IntentoCreate, id_usuario: int) -> Intento:
    """Crea un intento nuevo."""
    db_obj = Intento(
        calificacion=intento_in.calificacion,
        id_usuario=id_usuario,
        id_examen=intento_in.id_examen
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_intento(
    db: Session, 
    intento_id: int, 
    intento_in: IntentoUpdate
) -> Optional[Intento]:
    """Actualiza un intento existente."""
    db_obj = get_intento(db, intento_id=intento_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = intento_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_intento(db: Session, intento_id: int) -> Optional[Intento]:
    """Elimina un intento por su ID."""
    db_obj = get_intento(db, intento_id=intento_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_intentos(db: Session) -> int:
    """Cuenta el total de intentos en la base de datos."""
    return db.query(Intento).count()