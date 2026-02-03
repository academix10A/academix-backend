from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.tema import Tema
from app.schemas.tema import TemaCreate, TemaUpdate


def get_tema(db: Session, tema_id: int) -> Optional[Tema]:
    """Obtiene un tema por su ID."""
    return db.query(Tema).filter(Tema.id_tema == tema_id).first()


def get_tema_by_nombre(db: Session, nombre: str) -> Optional[Tema]:
    """Obtiene un tema por su nombre."""
    return db.query(Tema).filter(Tema.nombre == nombre).first()


def get_temas(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Tema]:
    """Obtiene una lista de temas con paginación."""
    return db.query(Tema).offset(skip).limit(limit).all()


def get_temas_by_dificultad(
    db: Session, 
    nivel_dificultad: str
) -> List[Tema]:
    """Obtiene temas filtrados por nivel de dificultad."""
    return db.query(Tema).filter(
        Tema.nivel_dificultad == nivel_dificultad
    ).all()


def create_tema(db: Session, tema_in: TemaCreate) -> Tema:
    """Crea un tema nuevo."""
    db_obj = Tema(
        nombre=tema_in.nombre,
        descripcion=tema_in.descripcion,
        nivel_dificultad=tema_in.nivel_dificultad
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_tema(
    db: Session, 
    tema_id: int, 
    tema_in: TemaUpdate
) -> Optional[Tema]:
    """Actualiza un tema existente."""
    db_obj = get_tema(db, tema_id=tema_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = tema_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_tema(db: Session, tema_id: int) -> Optional[Tema]:
    """Elimina un tema por su ID."""
    db_obj = get_tema(db, tema_id=tema_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_temas(db: Session) -> int:
    """Cuenta el total de temas en la base de datos."""
    return db.query(Tema).count()