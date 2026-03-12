from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.publicacion import Publicacion
from app.schemas.publicacion import PublicacionCreate, PublicacionUpdate


def get_publicacion(db: Session, publicacion_id: int) -> Optional[Publicacion]:
    """Obtiene un tema por su ID."""
    return db.query(Publicacion).filter(Publicacion.id_publicacion == publicacion_id).first()


def get_publicacion_by_titulo(db: Session, titulo: str) -> Optional[Publicacion]:
    """Obtiene un Publicacion por su Titulo."""
    return db.query(Publicacion).filter(Publicacion.titulo == titulo).first()


def get_publicaciones(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Publicacion]:
    """Obtiene una lista de Publicacion con paginación."""
    return db.query(Publicacion).offset(skip).limit(limit).all()


def create_publicacion(db: Session, publicacion_in: PublicacionCreate) -> Publicacion:
    """Crea un Publicacion nuevo."""
    db_obj = Publicacion(
        titulo=publicacion_in.titulo,
        descripcion=publicacion_in.descripcion,
        texto=publicacion_in.texto,
        id_usuario=publicacion_in.id_usuario,
        id_estado=publicacion_in.id_estado
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_Publicacion(
    db: Session, 
    publicacion_id: int, 
    publicacion_in: PublicacionUpdate
) -> Optional[Publicacion]:
    """Actualiza un Publicacion existente."""
    db_obj = get_publicacion(db, publicacion_id=publicacion_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = publicacion_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_publicacion(db: Session, publicacion_id: int) -> Optional[Publicacion]:
    """Elimina un Publicacion por su ID."""
    db_obj = get_publicacion(db, publicacion_id=publicacion_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_publicacion(db: Session) -> int:
    """Cuenta el total de publicaciones en la base de datos."""
    return db.query(Publicacion).count()