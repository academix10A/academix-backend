from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.examen import Examen
from app.schemas.examen import ExamenCreate, ExamenUpdate


def get_examen(db: Session, examen_id: int) -> Optional[Examen]:
    """Obtiene un tema por su ID."""
    return db.query(Examen).filter(Examen.id_examen == examen_id).first()


def get_examen_by_titulo(db: Session, titulo: str) -> Optional[Examen]:
    """Obtiene un examen por su Titulo."""
    return db.query(Examen).filter(Examen.titulo == titulo).first()


def get_examenes(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Examen]:
    """Obtiene una lista de examen con paginación."""
    return db.query(Examen).offset(skip).limit(limit).all()


def create_examen(db: Session, examen_in: ExamenCreate) -> Examen:
    """Crea un examen nuevo."""
    db_obj = Examen(
        titulo=examen_in.titulo,
        descripcion=examen_in.descripcion,
        cantidad_preguntas=examen_in.cantidad_preguntas,
        id_subtema=examen_in.id_subtema
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_examen(
    db: Session, 
    examen_id: int, 
    examen_in: ExamenUpdate
) -> Optional[Examen]:
    """Actualiza un examen existente."""
    db_obj = get_examen(db, examen_id=examen_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = examen_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_examen(db: Session, examen_id: int) -> Optional[Examen]:
    """Elimina un examen por su ID."""
    db_obj = get_examen(db, examen_id=examen_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_examen(db: Session) -> int:
    """Cuenta el total de examenes en la base de datos."""
    return db.query(Examen).count()