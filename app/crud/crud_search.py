from sqlalchemy import or_, func, exists, select
from sqlalchemy.orm import Session

from app.models.recurso import Recurso
from app.models.nota import Nota
from app.models.publicacion import Publicacion
from app.models.etiqueta import Etiqueta
from app.models.subtema import Subtema
from app.models.tema import Tema
from app.models.intermedias import recurso_etiqueta, tema_subtema, publicacion_etiqueta


def get_search(db: Session, q: str, type: str):
    results = []
    search_term = f"%{q.lower()}%"

    if type in ["all", "recursos"]:

        # ¿Existe alguna etiqueta con ese nombre ligada al recurso?
        tiene_etiqueta = (
            exists()
            .where(recurso_etiqueta.c.id_recurso == Recurso.id_recurso)
            .where(
                recurso_etiqueta.c.id_etiqueta.in_(
                    select(Etiqueta.id_etiqueta).where(
                        func.lower(Etiqueta.nombre).like(search_term)
                    )
                )
            )
        )

        # ¿El subtema del recurso coincide o pertenece a un tema que coincide?
        tiene_subtema = (
            exists()
            .where(Subtema.id_subtema == Recurso.id_subtema)
            .where(func.lower(Subtema.nombre).like(search_term))
        )

        tiene_tema = (
            exists()
            .where(Subtema.id_subtema == Recurso.id_subtema)
            .where(
                Subtema.id_subtema.in_(
                    select(tema_subtema.c.id_subtema).where(
                        tema_subtema.c.id_tema.in_(
                            select(Tema.id_tema).where(
                                func.lower(Tema.nombre).like(search_term)
                            )
                        )
                    )
                )
            )
        )

        recursos = (
            db.query(Recurso)
            .filter(
                or_(
                    func.lower(Recurso.titulo).like(search_term),
                    func.lower(Recurso.descripcion).like(search_term),
                    tiene_etiqueta,
                    tiene_subtema,
                    tiene_tema,
                )
            )
            .limit(10)
            .all()
        )

        for r in recursos:
            results.append({
                "id": r.id_recurso,
                "titulo": r.titulo,
                "descripcion": r.descripcion,
                "tipo": "RECURSO",
            })

    if type in ["all", "notas"]:

        # Etiqueta del recurso asociado a la nota
        tiene_etiqueta_nota = (
            exists()
            .where(Recurso.id_recurso == Nota.id_recurso)
            .where(
                recurso_etiqueta.c.id_recurso == Nota.id_recurso,
                recurso_etiqueta.c.id_etiqueta.in_(
                    select(Etiqueta.id_etiqueta).where(
                        func.lower(Etiqueta.nombre).like(search_term)
                    )
                ),
            )
        )

        # Subtema del recurso asociado a la nota
        tiene_subtema_nota = (
            exists()
            .where(Recurso.id_recurso == Nota.id_recurso)
            .where(
                Subtema.id_subtema == Recurso.id_subtema,
                func.lower(Subtema.nombre).like(search_term),
            )
        )

        # Tema del subtema del recurso asociado a la nota
        tiene_tema_nota = (
            exists()
            .where(Recurso.id_recurso == Nota.id_recurso)
            .where(Subtema.id_subtema == Recurso.id_subtema)
            .where(
                Subtema.id_subtema.in_(
                    select(tema_subtema.c.id_subtema).where(
                        tema_subtema.c.id_tema.in_(
                            select(Tema.id_tema).where(
                                func.lower(Tema.nombre).like(search_term)
                            )
                        )
                    )
                )
            )
        )

        notas = (
            db.query(Nota)
            .filter(
                Nota.es_compartida.is_(True),
                or_(
                    func.lower(Nota.titulo).like(search_term),
                    func.lower(Nota.contenido).like(search_term),
                    tiene_etiqueta_nota,
                    tiene_subtema_nota,
                    tiene_tema_nota,
                ),
            )
            .limit(10)
            .all()
        )

        for n in notas:
            results.append({
                "id": n.id_nota,
                "titulo": n.titulo,
                "descripcion": n.contenido[:100],
                "usuario": f"{n.usuario.nombre} {n.usuario.apellido_paterno}",
                "tipo": "NOTA",
            })

    if type in ["all", "publicaciones"]:

        tiene_etiqueta_pub = (
            exists()
            .where(publicacion_etiqueta.c.id_publicacion == Publicacion.id_publicacion)
            .where(
                publicacion_etiqueta.c.id_etiqueta.in_(
                    select(Etiqueta.id_etiqueta).where(
                        func.lower(Etiqueta.nombre).like(search_term)
                    )
                )
            )
        )

        publicaciones = (
            db.query(Publicacion)
            .filter(
                or_(
                    func.lower(Publicacion.titulo).like(search_term),
                    func.lower(Publicacion.descripcion).like(search_term),
                    func.lower(Publicacion.texto).like(search_term),
                    tiene_etiqueta_pub,
                )
            )
            .limit(10)
            .all()
        )

        for p in publicaciones:
            results.append({
                "id": p.id_publicacion,
                "titulo": p.titulo,
                "descripcion": p.descripcion,
                "usuario": f"{p.usuario.nombre} {p.usuario.apellido_paterno}",
                "tipo": "PUBLICACION",
            })

    if type in ["all", "temas"]:

        tiene_subtema_tema = (
            exists()
            .where(tema_subtema.c.id_tema == Tema.id_tema)
            .where(
                tema_subtema.c.id_subtema.in_(
                    select(Subtema.id_subtema).where(
                        or_(
                            func.lower(Subtema.nombre).like(search_term),
                            func.lower(Subtema.descripcion).like(search_term),
                        )
                    )
                )
            )
        )

        temas = (
            db.query(Tema)
            .filter(
                or_(
                    func.lower(Tema.nombre).like(search_term),
                    func.lower(Tema.descripcion).like(search_term),
                    tiene_subtema_tema,
                )
            )
            .limit(10)
            .all()
        )

        for t in temas:
            results.append({
                "id": t.id_tema,
                "titulo": t.nombre,
                "descripcion": t.descripcion,
                "tipo": "TEMA",
            })

    return {
        "busqueda": q,
        "total": len(results),
        "resultados": results,
    }