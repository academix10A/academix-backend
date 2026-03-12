from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.beneficio import Beneficio
from app.models.membresia import Membresia
from app.schemas.membresia import MembresiaCreate, MembresiaUpdate


def get_membresia(db: Session, membresia_id: int) -> Optional[Membresia]:
    """Obtiene un rol por su ID."""
    return db.query(Membresia).filter(Membresia.id_membresia == membresia_id).first()


def get_membresia_by_nombre(db: Session, nombre: str) -> Optional[Membresia]:
    """Obtiene un membresia por su nombre."""
    return db.query(Membresia).filter(Membresia.nombre == nombre).first()


def get_membresias(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
) -> List[Membresia]:
    """Obtiene una lista de membresia con paginación."""
    return db.query(Membresia).offset(skip).limit(limit).all()

def create_membresia(db: Session, membresia_in: MembresiaCreate) -> Membresia:
    db_obj = Membresia(
        nombre=membresia_in.nombre,
        descripcion=membresia_in.descripcion,
        costo=membresia_in.costo,
        tipo=membresia_in.tipo,
        fecha_inicio=membresia_in.fecha_inicio,
        fecha_fin=membresia_in.fecha_fin,
        id_estado=membresia_in.id_estado,
    )
    db.add(db_obj)
    db.flush()  # genera el id_membresia sin hacer commit

    # Asociar beneficios a través de la tabla intermedia
    if membresia_in.beneficios_ids:
        beneficios = db.query(Beneficio).filter(
            Beneficio.id_beneficio.in_(membresia_in.beneficios_ids)
        ).all()
        db_obj.beneficios = beneficios  # SQLAlchemy maneja la tabla intermedia solo

    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_membresia(
    db: Session, 
    membresia_id: int, 
    membresia_in: MembresiaUpdate
) -> Optional[Membresia]:
    """Actualiza un membresia existente."""
    db_obj = get_membresia(db, membresia_id=membresia_id)
    if not db_obj:
        return None
    
    # Actualizar solo los campos que vienen en el request
    update_data = membresia_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_membresia(db: Session, membresia_id: int) -> Optional[Membresia]:
    """Elimina un membresia por su ID."""
    db_obj = get_membresia(db, membresia_id=membresia_id)
    if not db_obj:
        return None
    
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_membresia(db: Session) -> int:
    """Cuenta el total de membresia en la base de datos."""
    return db.query(Membresia).count()