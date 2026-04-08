# app/crud/crud_publicacion.py
from typing import Optional, List, Tuple

from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_, func

from app.models.publicacion import Publicacion
from app.models.etiqueta import Etiqueta
from app.models.usuario import Usuario
from app.schemas.publicacion import PublicacionCreate, PublicacionUpdate


# ── Helpers internos ──────────────────────────────────────────────────────────

def _apply_filters(query, titulo: Optional[str], nombre_usuario: Optional[str], etiqueta: Optional[str]):
    """Aplica los filtros de búsqueda a un query base."""
    if titulo:
        query = query.filter(Publicacion.titulo.ilike(f"%{titulo}%"))

    if nombre_usuario:
        query = query.join(Publicacion.usuario).filter(
            or_(
                Usuario.nombre.ilike(f"%{nombre_usuario}%"),
                Usuario.apellido_paterno.ilike(f"%{nombre_usuario}%"),
            )
        )

    if etiqueta:
        query = query.join(Publicacion.etiquetas).filter(
            Etiqueta.nombre.ilike(f"%{etiqueta}%")
        )

    return query


# ── Lecturas ──────────────────────────────────────────────────────────────────

def get_publicacion(db: Session, publicacion_id: int) -> Optional[Publicacion]:
    """Obtiene una publicación por ID con usuario y etiquetas."""
    return (
        db.query(Publicacion)
        .options(joinedload(Publicacion.usuario), joinedload(Publicacion.etiquetas))
        .filter(Publicacion.id_publicacion == publicacion_id)
        .first()
    )


def get_publicacion_by_titulo(db: Session, titulo: str) -> Optional[Publicacion]:
    return db.query(Publicacion).filter(Publicacion.titulo == titulo).first()


def get_publicaciones(
    db: Session,
    skip: int = 0,
    limit: int = 20,
    titulo: Optional[str] = None,
    nombre_usuario: Optional[str] = None,
    etiqueta: Optional[str] = None,
) -> Tuple[List[Publicacion], int]:
    """
    Retorna una tupla (items, total) con soporte de búsqueda y paginación.
    - titulo: busca en el título (ilike)
    - nombre_usuario: busca en nombre o apellido paterno del autor
    - etiqueta: busca en el nombre de la etiqueta
    """
    base_query = (
        db.query(Publicacion)
        .options(joinedload(Publicacion.usuario), joinedload(Publicacion.etiquetas))
    )

    base_query = _apply_filters(base_query, titulo, nombre_usuario, etiqueta)

    # Contar antes de paginar
    total = (
        db.query(func.count(Publicacion.id_publicacion.distinct()))
        .select_from(Publicacion)
    )
    total = _apply_filters(total, titulo, nombre_usuario, etiqueta).scalar()

    items = (
        base_query
        .order_by(Publicacion.fecha_creacion.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return items, total


# ── Escritura ─────────────────────────────────────────────────────────────────

def create_publicacion(
    db: Session,
    publicacion_in: PublicacionCreate,
    id_usuario: int,
) -> Publicacion:
    """Crea una publicación. El id_usuario siempre viene del token JWT."""
    db_obj = Publicacion(
        titulo      = publicacion_in.titulo,
        descripcion = publicacion_in.descripcion,
        texto       = publicacion_in.texto,
        id_usuario  = id_usuario,
        id_estado   = publicacion_in.id_estado,
    )

    # Asociar etiquetas si se enviaron IDs
    if publicacion_in.etiquetas:
        etiquetas = db.query(Etiqueta).filter(
            Etiqueta.id_etiqueta.in_(publicacion_in.etiquetas)
        ).all()
        db_obj.etiquetas = etiquetas

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_publicacion(
    db: Session,
    publicacion_id: int,
    publicacion_in: PublicacionUpdate,
) -> Optional[Publicacion]:
    db_obj = get_publicacion(db, publicacion_id)
    if not db_obj:
        return None

    update_data = publicacion_in.model_dump(exclude_unset=True)

    # Manejar etiquetas por separado
    etiqueta_ids = update_data.pop("etiquetas", None)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    if etiqueta_ids is not None:
        etiquetas = db.query(Etiqueta).filter(
            Etiqueta.id_etiqueta.in_(etiqueta_ids)
        ).all()
        db_obj.etiquetas = etiquetas

    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_publicacion(db: Session, publicacion_id: int) -> Optional[Publicacion]:
    db_obj = get_publicacion(db, publicacion_id)
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj


def count_publicacion(db: Session) -> int:
    return db.query(Publicacion).count()
