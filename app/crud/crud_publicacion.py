# app/crud/crud_publicacion.py
from typing import Optional, List, Tuple

from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_, func

from app.models.publicacion import Publicacion
from app.models.etiqueta import Etiqueta
from app.models.usuario import Usuario
from app.schemas.publicacion import PublicacionCreate, PublicacionUpdate

DEFAULT_ID_ESTADO = 4


# ── Helpers internos ──────────────────────────────────────────────────────────

def _apply_filters(
    query,
    titulo: Optional[str] = None,
    nombre_usuario: Optional[str] = None,
    etiqueta: Optional[str] = None,
):
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


def _resolver_etiquetas_por_nombre(db: Session, nombres: List[str]) -> List[Etiqueta]:
    """
    Dado una lista de nombres de etiquetas, devuelve los objetos Etiqueta
    correspondientes. Si una etiqueta no existe, la crea automáticamente.
    """
    etiquetas = []
    for nombre in nombres:
        nombre = nombre.strip()
        if not nombre:
            continue
        etiqueta = db.query(Etiqueta).filter(Etiqueta.nombre == nombre).first()
        if not etiqueta:
            etiqueta = Etiqueta(nombre=nombre)
            db.add(etiqueta)
            db.flush()  # Obtener el ID sin hacer commit todavía
        etiquetas.append(etiqueta)
    return etiquetas


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
    total_query = (
        db.query(func.count(Publicacion.id_publicacion.distinct()))
        .select_from(Publicacion)
    )
    total = _apply_filters(total_query, titulo, nombre_usuario, etiqueta).scalar()

    items = (
        base_query
        .order_by(Publicacion.fecha_creacion.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return items, total


def get_publicacion_by_usuario(
    db: Session,
    id_usuario: int,
    skip: int = 0,
    limit: int = 100,
) -> List[Publicacion]:
    """Obtiene solo las publicaciones que pertenecen a un usuario específico."""
    return (
        db.query(Publicacion)
        .options(joinedload(Publicacion.usuario), joinedload(Publicacion.etiquetas))
        .filter(Publicacion.id_usuario == id_usuario)
        .order_by(Publicacion.fecha_creacion.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


# ── Escritura ─────────────────────────────────────────────────────────────────

def create_publicacion(
    db: Session,
    publicacion_in: PublicacionCreate,
    id_usuario: int,
) -> Publicacion:
    """
    Crea una publicación. El id_usuario siempre viene del token JWT.
    - etiquetas: acepta lista de strings (nombres). Las crea si no existen.
    - id_estado: usa el valor del schema o DEFAULT_ID_ESTADO si no se envía.
    """
    db_obj = Publicacion(
        titulo      = publicacion_in.titulo,
        descripcion = publicacion_in.descripcion,
        texto       = publicacion_in.texto,
        id_usuario  = id_usuario,
        id_estado   = publicacion_in.id_estado if publicacion_in.id_estado is not None else DEFAULT_ID_ESTADO,
    )

    # Resolver etiquetas por nombre (strings) — las crea si no existen
    if publicacion_in.etiquetas:
        db_obj.etiquetas = _resolver_etiquetas_por_nombre(db, publicacion_in.etiquetas)

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

    # Manejar etiquetas por separado (vienen como strings)
    etiqueta_nombres = update_data.pop("etiquetas", None)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    if etiqueta_nombres is not None:
        db_obj.etiquetas = _resolver_etiquetas_por_nombre(db, etiqueta_nombres)

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