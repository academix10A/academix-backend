from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.recurso import Recurso
from app.schemas.recurso import RecursoCreate, RecursoUpdate
from app.models.etiqueta import Etiqueta


def get_recurso(db: Session, recurso_id: int) -> Optional[Recurso]:
    """Obtiene un Recurso por su ID."""
    return db.query(Recurso).filter(Recurso.id_recurso == recurso_id).first()


def get_recurso_by_titulo(db: Session, titulo: str) -> Optional[Recurso]:
    """Obtiene un recurso por su Titulo."""
    return db.query(Recurso).filter(Recurso.titulo == titulo).first()

def get_recurso_by_url(db: Session, url_archivo: str) -> Optional[Recurso]:
    """Obtiene un recurso por su url."""
    return db.query(Recurso).filter(Recurso.url_archivo == url_archivo).first()

def get_recurso_by_contenido(db: Session, contenido: str) -> Optional[Recurso]:
    """Obtiene un recurso por su contenido."""
    return db.query(Recurso).filter(Recurso.contenido == contenido).first()

def get_recursos(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Recurso]:
    """Obtiene una lista de recurso con paginación."""
    return db.query(Recurso).offset(skip).limit(limit).all()


def create_recurso(db: Session, recurso_in: RecursoCreate) -> Recurso:
    """Crea un recurso y lo vincula con una etiqueta usando su ID."""
    db_obj = Recurso(
        titulo=recurso_in.titulo,
        descripcion=recurso_in.descripcion,
        contenido=recurso_in.contenido,
        url_archivo=recurso_in.url_archivo,
        id_tipo=recurso_in.id_tipo, 
        id_estado=recurso_in.id_estado, 
        id_subtema=recurso_in.id_subtema 
    )

    if recurso_in.id_etiqueta:
        # Buscamos la etiqueta en la DB para asegurarnos de que el ID es válido
        etiqueta = db.query(Etiqueta).filter(Etiqueta.id_etiqueta == recurso_in.id_etiqueta).first()
        
        if etiqueta:
            # .append() le dice a SQLAlchemy: "Crea un registro en recurso_etiqueta" 
            db_obj.etiquetas.append(etiqueta)
        else:
            # Opcional: Podrías lanzar un error si el ID de etiqueta no existe
            pass

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_recurso(
    db: Session, 
    recurso_id: int, 
    recurso_in: RecursoUpdate
) -> Optional[Recurso]:
    """Actualiza un recurso existente."""
    db_obj = get_recurso(db, recurso_id=recurso_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = recurso_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_recurso(db: Session, recurso_id: int) -> Optional[Recurso]:
    """Elimina un recurso por su ID."""
    db_obj = get_recurso(db, recurso_id=recurso_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_recurso(db: Session) -> int:
    """Cuenta el total de recurso en la base de datos."""
    return db.query(Recurso).count()