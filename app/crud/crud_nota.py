from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.nota import Nota
from app.schemas.nota import NotaCreate, NotaUpdate


def get_nota(db: Session, nota_id: int) -> Optional[Nota]:
    """Obtiene un nota por su ID."""
    return db.query(Nota).filter(Nota.id_nota == nota_id).first()

def get_notas(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Nota]:
    """Obtiene una lista de Notas con paginación."""
    return db.query(Nota).offset(skip).limit(limit).all()


def get_nota_by_contenido(db: Session, contenido: str) -> Optional[Nota]:
    """Obtiene un recurso por su contenido."""
    return db.query(Nota).filter(Nota.contenido == contenido).first()


def create_nota(db: Session, nota_in: NotaCreate) -> Nota:
    """Crea un nota nuevo."""
    db_obj = Nota(
        contenido=nota_in.contenido,
        es_compartida=nota_in.es_compartida,
        id_usuario=nota_in.id_usuario,
        id_recurso=nota_in.id_recurso
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_nota(
    db: Session, 
    nota_id: int, 
    nota_in: NotaUpdate
) -> Optional[Nota]:
    """Actualiza un nota existente."""
    db_obj = get_nota(db, nota_id=nota_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = nota_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_nota(db: Session, nota_id: int) -> Optional[Nota]:
    """Elimina un nota por su ID."""
    db_obj = get_nota(db, nota_id=nota_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_notas(db: Session) -> int:
    """Cuenta el total de notas en la base de datos."""
    return db.query(Nota).count()