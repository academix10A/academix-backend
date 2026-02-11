from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.pregunta import Pregunta
from app.schemas.pregunta import PreguntaCreate, PreguntaUpdate


def get_pregunta(db: Session, pregunta_id: int) -> Optional[Pregunta]:
    """Obtiene un pregunta por su ID."""
    return db.query(Pregunta).filter(Pregunta.id_pregunta == pregunta_id).first()

def get_preguntas(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Pregunta]:
    """Obtiene una lista de Preguntas con paginación."""
    return db.query(Pregunta).offset(skip).limit(limit).all()


def get_pregunta_by_contenido(db: Session, contenido: str) -> Optional[Pregunta]:
    """Obtiene un recurso por su contenido."""
    return db.query(Pregunta).filter(Pregunta.contenido == contenido).first()


def create_pregunta(db: Session, pregunta_in: PreguntaCreate) -> Pregunta:
    """Crea un pregunta nuevo."""
    db_obj = Pregunta(
        contenido=pregunta_in.contenido,
        id_examen=pregunta_in.id_examen,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_pregunta(
    db: Session, 
    pregunta_id: int, 
    pregunta_in: PreguntaUpdate
) -> Optional[Pregunta]:
    """Actualiza un pregunta existente."""
    db_obj = get_pregunta(db, pregunta_id=pregunta_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = pregunta_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_pregunta(db: Session, pregunta_id: int) -> Optional[Pregunta]:
    """Elimina un pregunta por su ID."""
    db_obj = get_pregunta(db, pregunta_id=pregunta_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_preguntas(db: Session) -> int:
    """Cuenta el total de preguntas en la base de datos."""
    return db.query(Pregunta).count()