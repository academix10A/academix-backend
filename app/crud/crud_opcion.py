from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.opcion import Opcion
from app.schemas.opcion import OpcionCreate, OpcionUpdate


def get_opcion(db: Session, opcion_id: int) -> Optional[Opcion]:
    """Obtiene un opcion por su ID."""
    return db.query(Opcion).filter(Opcion.id_opcion == opcion_id).first()

def get_opciones(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Opcion]:
    """Obtiene una lista de Opcions con paginación."""
    return db.query(Opcion).offset(skip).limit(limit).all()


def get_opcion_by_respuesta(db: Session, respuesta: str) -> Optional[Opcion]:
    """Obtiene un opcion por su respuesta."""
    return db.query(Opcion).filter(Opcion.respuesta == respuesta).first()


def create_opcion(db: Session, opcion_in: OpcionCreate) -> Opcion:
    """Crea un opcion nuevo."""
    db_obj = Opcion(
        respuesta=opcion_in.respuesta,
        es_correcta=opcion_in.es_correcta,
        id_pregunta=opcion_in.id_pregunta,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_opcion(
    db: Session, 
    opcion_id: int, 
    opcion_in: OpcionUpdate
) -> Optional[Opcion]:
    """Actualiza un opcion existente."""
    db_obj = get_opcion(db, opcion_id=opcion_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = opcion_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_opcion(db: Session, opcion_id: int) -> Optional[Opcion]:
    """Elimina un opcion por su ID."""
    db_obj = get_opcion(db, opcion_id=opcion_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_opcions(db: Session) -> int:
    """Cuenta el total de opcions en la base de datos."""
    return db.query(Opcion).count()