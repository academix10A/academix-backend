from fastapi import APIRouter
from sqlalchemy import or_, func

from app.models.recurso import Recurso
from app.models.nota import Nota
from app.models.subtema import Subtema

router = APIRouter()

def get_search(db, q, type):
    results = []
    search_term = f"%{q.lower()}%"
    if type in ["all", "recursos"]:
        recursos = db.query(Recurso).filter(
            or_(
                func.lower(Recurso.titulo).like(search_term),
                func.lower(Recurso.descripcion).like(search_term)
            )
        ).limit(10).all()

        for r in recursos:
            results.append({
                "id": r.id_recurso,
                "titulo": r.titulo,
                "descripcion": r.descripcion,
                "tipo": "RECURSO"
            })
    if type in ["all", "notas"]:
        notas = db.query(Nota).filter(
            Nota.es_compartida.is_(True),
            func.lower(Nota.contenido).like(search_term)
        ).limit(10).all()

        for n in notas:
            results.append({
                "id": n.id_nota,
                "titulo": "Nota",
                "descripcion": n.contenido[:100],
                "usuario": f"{n.usuario.nombre} {n.usuario.apellido_paterno}",
                "tipo": "NOTA"
            })
    if type in ["all", "temas"]:
        temas = db.query(Subtema).filter(
            func.lower(Subtema.nombre).like(search_term)
        ).limit(10).all()

        for t in temas:
            results.append({
                "id": t.id_subtema,
                "titulo": t.nombre,
                "descripcion": t.descripcion,
                "tipo": "TEMA"
            })
    return {
        "busqueda": q,
        "total": len(results),
        "resultados": results
    }


