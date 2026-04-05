from typing import Optional, List

from sqlalchemy.orm import Session
from sqlalchemy import func, case

from app.models.examen import Examen
from app.schemas.examen import ExamenCreate, ExamenUpdate
from app.models.intento import Intento
from app.models.subtema import Subtema
from app.models.intermedias import respuesta_intento


def get_examenes_realizados_por_usuario(db: Session, id_usuario: int):
    return (
        db.query(
            Intento.id_intento,
            Intento.id_examen,
            Examen.titulo.label("titulo_examen"),
            Intento.calificacion,
            Intento.fecha
        )
        .join(Examen)
        .filter(Intento.id_usuario == id_usuario)
        .all()
    )


def get_examenes_filtrados(
    db: Session,
    solo_basicos: bool,
    skip: int = 0,
    limit: int = 100,
    excluir_realizados_por: Optional[int] = None  # id_usuario para freemium
) -> List[Examen]:
    """
    Obtiene exámenes con filtros:
    - solo_basicos: si True, solo devuelve básicos
    - excluir_realizados_por: si se pasa un id_usuario, excluye los que ya contestó
    """
    query = db.query(Examen).join(Examen.subtema)

    if solo_basicos:
        query = query.filter(func.lower(Subtema.nivel_dificultad) == "basico")

    if excluir_realizados_por is not None:
        # Subconsulta: IDs de exámenes donde el usuario ya tiene 2 o más intentos
        ya_agotados = (
            db.query(Intento.id_examen)
            .filter(Intento.id_usuario == excluir_realizados_por)
            .group_by(Intento.id_examen)
            .having(func.count(Intento.id_intento) >= 2)
            .subquery()
        )
        query = query.filter(Examen.id_examen.not_in(ya_agotados))

    return query.offset(skip).limit(limit).all()


def get_intentos_por_examen(
    db: Session,
    id_usuario: int,
    id_examen: int
) -> List[Intento]:
    """
    Devuelve todos los intentos de un usuario en un examen específico,
    ordenados del más reciente al más antiguo.
    """
    return (
        db.query(Intento)
        .filter(
            Intento.id_usuario == id_usuario,
            Intento.id_examen == id_examen
        )
        .order_by(Intento.fecha.desc())
        .all()
    )

def get_examenes_realizados_detalle(db: Session, id_usuario: int):
    correctas_sq = (
        db.query(
            respuesta_intento.c.id_intento,
            func.sum(
                case((respuesta_intento.c.es_correcta == True, 1), else_=0)
            ).label("respuestas_correctas"),
            func.count(respuesta_intento.c.id_pregunta).label("cantidad_preguntas"),
        )
        .group_by(respuesta_intento.c.id_intento)
        .subquery()
    )

    rows = (
        db.query(
            Intento.id_intento,
            Intento.id_examen,
            Examen.titulo.label("titulo_examen"),
            Intento.calificacion,
            Intento.fecha,
            correctas_sq.c.respuestas_correctas,
            correctas_sq.c.cantidad_preguntas,
        )
        .join(Examen, Intento.id_examen == Examen.id_examen)
        .outerjoin(correctas_sq, Intento.id_intento == correctas_sq.c.id_intento)
        .filter(Intento.id_usuario == id_usuario)
        .all()
    )

    result = []
    for r in rows:
        correctas = r.respuestas_correctas or 0
        total = r.cantidad_preguntas or 0
        porcentaje = round((correctas / total) * 100, 2) if total > 0 else r.calificacion * 10
        result.append({
            "id_intento": r.id_intento,
            "id_examen": r.id_examen,
            "titulo_examen": r.titulo_examen,
            "calificacion": r.calificacion,
            "fecha": r.fecha,
            "respuestas_correctas": correctas,
            "cantidad_preguntas": total,
            "aprobo": porcentaje >= 70,
            "porcentaje": porcentaje,
        })
    return result

def get_examen(db: Session, examen_id: int) -> Optional[Examen]:
    """Obtiene un examen por su ID."""
    return db.query(Examen).filter(Examen.id_examen == examen_id).first()


def get_examen_by_titulo(db: Session, titulo: str) -> Optional[Examen]:
    """Obtiene un examen por su Titulo."""
    return db.query(Examen).filter(Examen.titulo == titulo).first()


def get_examenes(
    db: Session,
    skip: int = 0,
    limit: int = 100
) -> List[Examen]:
    """Obtiene una lista de examen con paginación."""
    return db.query(Examen).offset(skip).limit(limit).all()


def create_examen(db: Session, examen_in: ExamenCreate) -> Examen:
    """Crea un examen nuevo."""
    db_obj = Examen(
        titulo=examen_in.titulo,
        descripcion=examen_in.descripcion,
        cantidad_preguntas=examen_in.cantidad_preguntas,
        id_subtema=examen_in.id_subtema
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_examen(
    db: Session,
    examen_id: int,
    examen_in: ExamenUpdate
) -> Optional[Examen]:
    """Actualiza un examen existente."""
    db_obj = get_examen(db, examen_id=examen_id)
    if not db_obj:
        return None

    update_data = examen_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_examen(db: Session, examen_id: int) -> Optional[Examen]:
    """Elimina un examen por su ID."""
    db_obj = get_examen(db, examen_id=examen_id)
    if not db_obj:
        return None

    db.delete(db_obj)
    db.commit()
    return db_obj


def count_examen(db: Session) -> int:
    """Cuenta el total de examenes en la base de datos."""
    return db.query(Examen).count()