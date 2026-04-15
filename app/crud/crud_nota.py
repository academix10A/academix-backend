# app/crud/crud_nota.py
from typing import Optional, List
from sqlalchemy.orm import Session, joinedload
from app.models.nota import Nota
from app.schemas.nota import NotaCreate, NotaUpdate


def get_nota(db: Session, nota_id: int) -> Optional[Nota]:
    """Obtiene una nota por su ID."""
    return db.query(Nota).filter(Nota.id_nota == nota_id).first()


def get_notas(db: Session, skip: int = 0, limit: int = 100) -> List[Nota]:
    """Obtiene todas las notas (solo para admin)."""
    return db.query(Nota).offset(skip).limit(limit).all()


def get_notas_by_usuario(
    db: Session,
    id_usuario: int,
    skip: int = 0,
    limit: int = 100,
) -> List[Nota]:
    """Obtiene solo las notas que pertenecen a un usuario específico."""
    return (
        db.query(Nota)
        .options(joinedload(Nota.recurso))
        .filter(Nota.id_usuario == id_usuario)
        .order_by(Nota.fecha_creacion.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

def count_notas_por_usuario(
    db: Session,
    id_usuario: int
) -> dict:
    """Cuenta cuántas notas tiene un usuario."""
    data = db.query(Nota).filter(Nota.id_usuario == id_usuario).count()
    return {"count": data}

def get_notas_compartidas(
    db: Session, skip: int = 0, limit: int = 100
) -> List[Nota]:
    """Obtiene todas las notas marcadas como compartidas."""
    return (
        db.query(Nota)
        .options(joinedload(Nota.usuario))
        .filter(Nota.es_compartida == True)
        .order_by(Nota.fecha_creacion.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_nota_by_contenido(db: Session, contenido: str) -> Optional[Nota]:
    """Busca una nota por contenido exacto (sin filtrar por usuario)."""
    return db.query(Nota).filter(Nota.contenido == contenido).first()


def get_nota_by_contenido_y_usuario(
    db: Session, contenido: str, id_usuario: int
) -> Optional[Nota]:
    """
    Busca si el mismo usuario ya tiene una nota con ese contenido exacto.
    Usado para evitar duplicados dentro del mismo usuario.
    """
    return (
        db.query(Nota)
        .filter(
            Nota.contenido == contenido,
            Nota.id_usuario == id_usuario,
        )
        .first()
    )

def get_notas_compartidas_by_recurso(
    db: Session,
    id_recurso: int
) -> List[Nota]:
    """Obtiene todas las notas compartidas de un recurso específico."""
    return (
        db.query(Nota)
        .filter(
            Nota.id_recurso == id_recurso,
            Nota.es_compartida == True
        )
        .order_by(Nota.fecha_creacion.desc())
        .all()
    )

def create_nota(db: Session, nota_in: NotaCreate, id_usuario: int) -> Nota:
    db_obj = Nota(
        titulo=nota_in.titulo,
        contenido=nota_in.contenido,
        es_compartida=nota_in.es_compartida,
        id_usuario=id_usuario,
        id_recurso=nota_in.id_recurso,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_nota(
    db: Session, nota_id: int, nota_in: NotaUpdate
) -> Optional[Nota]:
    """Actualiza una nota existente. Solo actualiza los campos enviados."""
    db_obj = get_nota(db, nota_id=nota_id)
    if not db_obj:
        return None

    update_data = nota_in.model_dump(exclude_unset=True)

    # No permitir cambiar id_usuario desde el update
    update_data.pop("id_usuario", None)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_nota(db: Session, nota_id: int) -> Optional[Nota]:
    """Elimina una nota por su ID."""
    db_obj = get_nota(db, nota_id=nota_id)
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_notas(db: Session) -> int:
    """Cuenta el total de notas."""
    return db.query(Nota).count()


def count_notas_by_usuario(db: Session, id_usuario: int) -> int:
    """Cuenta las notas de un usuario específico."""
    return db.query(Nota).filter(Nota.id_usuario == id_usuario).count()