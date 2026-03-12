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


def get_notas_usuario(
    db: Session, 
    id_usuario: int,
    skip: int = 0, 
    limit: int = 20
) -> List[Nota]:
    """Obtiene todas las notas (privadas + compartidas) de un usuario específico."""
    return db.query(Nota).filter(
        Nota.id_usuario == id_usuario
    ).order_by(Nota.fecha_actualizacion.desc()).offset(skip).limit(limit).all()


def get_notas_privadas_usuario(
    db: Session, 
    id_usuario: int,
    skip: int = 0, 
    limit: int = 20
) -> List[Nota]:
    """Obtiene solo las notas privadas de un usuario específico."""
    return db.query(Nota).filter(
        Nota.id_usuario == id_usuario,
        Nota.es_compartida == False
    ).order_by(Nota.fecha_actualizacion.desc()).offset(skip).limit(limit).all()


def get_notas_compartidas_usuario(
    db: Session, 
    id_usuario: int,
    skip: int = 0, 
    limit: int = 20
) -> List[Nota]:
    """Obtiene las notas compartidas de un usuario específico."""
    return db.query(Nota).filter(
        Nota.id_usuario == id_usuario,
        Nota.es_compartida == True
    ).order_by(Nota.fecha_actualizacion.desc()).offset(skip).limit(limit).all()


def get_nota_by_contenido(db: Session, contenido: str) -> Optional[Nota]:
    """Obtiene un recurso por su contenido."""
    return db.query(Nota).filter(Nota.contenido == contenido).first()


def create_nota(db: Session, nota_in: NotaCreate, id_usuario: int) -> Nota:
    """Crea un nota nuevo."""
    db_obj = Nota(
        contenido=nota_in.contenido,
        es_compartida=nota_in.es_compartida,
        id_usuario=id_usuario,
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