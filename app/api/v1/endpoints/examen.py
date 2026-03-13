# examen.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.crud import crud_examen
from app.schemas.examen import Examen, ExamenCreate, ExamenUpdate
from app.core.permissions import PermissionChecker
from app.schemas.examen import ExamenCompleto, ExamenSubmit, ExamenResultado
from app.models.pregunta import Pregunta
from app.models.opcion import Opcion
from app.models.intento import Intento
from app.models.intermedias import respuesta_intento
from datetime import datetime


router = APIRouter(prefix="/examen", tags=["examenes"])

solo_admin = PermissionChecker(roles=["admin"])
usuarios_activos = PermissionChecker(membresias=["premium", "gratis"])

@router.get("/", response_model=List[Examen], dependencies=[Depends(usuarios_activos)])
def list_examen(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Lista todos los examen con paginación."""
    examenes = crud_examen.get_examenes(db, skip=skip, limit=limit)
    return examenes

@router.get("/titulo/{titulo}", response_model=Examen,dependencies=[Depends(usuarios_activos)])
def get_examen_by_titulo(titulo: str, db: Session = Depends(get_db)):
    """Obtiene un examen por nombre."""
    examen = crud_examen.get_examen_by_titulo(db, titulo=titulo)
    if not examen:
        raise HTTPException(
            status_code=404, 
            detail=f"Examen '{titulo}' no encontrado"
        )
    return examen

@router.get("/{examen_id}", response_model=Examen, dependencies=[Depends(usuarios_activos)])
def read_examen(examen_id: int, db: Session = Depends(get_db)):
    """Obtiene un examen por ID."""
    examen = crud_examen.get_examen(db, examen_id=examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="examen no encontrado")
    return examen

@router.post("/", response_model=Examen, status_code=201, dependencies=[Depends(solo_admin)])
def create_examen(examen_in: ExamenCreate, db: Session = Depends(get_db)):
    """Crea un nuevo examen."""
    # Validar que no exista examen con ese titulo
    examen_exists = crud_examen.get_examen_by_titulo(db, titulo=examen_in.titulo)
    if examen_exists:
        raise HTTPException(
            status_code=400, 
            detail="Ya existe un examen con ese titulo"
        )
    
    examen = crud_examen.create_examen(db, examen_in=examen_in)
    return examen

@router.get("/{examen_id}/completo", response_model=ExamenCompleto, dependencies=[Depends(usuarios_activos)])
def get_examen_completo(examen_id: int, db: Session = Depends(get_db)):
    """
    Devuelve el examen con todas sus preguntas y opciones.
    Las opciones NO incluyen es_correcta para evitar trampa.
    """
    examen = crud_examen.get_examen(db, examen_id=examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")

    # Cargar preguntas con sus opciones
    preguntas = db.query(Pregunta).filter(Pregunta.id_examen == examen_id).all()
    if not preguntas:
        raise HTTPException(status_code=404, detail="Este examen no tiene preguntas aún")

    preguntas_con_opciones = []
    for p in preguntas:
        opciones = db.query(Opcion).filter(Opcion.id_pregunta == p.id_pregunta).all()
        preguntas_con_opciones.append({
            "id_pregunta": p.id_pregunta,
            "contenido":   p.contenido,
            "opciones": [
                {"id_opcion": o.id_opcion, "respuesta": o.respuesta}
                for o in opciones
            ]
        })

    return {
        "id_examen":          examen.id_examen,
        "titulo":             examen.titulo,
        "descripcion":        examen.descripcion,
        "cantidad_preguntas": examen.cantidad_preguntas,
        "id_subtema":         examen.id_subtema,
        "preguntas":          preguntas_con_opciones,
    }


@router.post("/submit", response_model=ExamenResultado, dependencies=[Depends(usuarios_activos)])
def submit_examen(submit_in: ExamenSubmit, db: Session = Depends(get_db)):
    """
    Recibe las respuestas del usuario, calcula la calificación,
    guarda el intento y las respuestas individuales en una sola llamada.
    """
    # 1 — Validar que el examen existe
    examen = crud_examen.get_examen(db, examen_id=submit_in.id_examen)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")

    # 2 — Validar que el usuario no haya hecho este examen antes
    intento_existente = db.query(Intento).filter(
        Intento.id_usuario == submit_in.id_usuario,
        Intento.id_examen  == submit_in.id_examen
    ).first()
    if intento_existente:
        raise HTTPException(
            status_code=400,
            detail="Ya realizaste este examen. Solo se permite un intento."
        )

    # 3 — Evaluar cada respuesta
    correctas = 0
    total     = len(submit_in.respuestas)
    detalles  = []

    for resp in submit_in.respuestas:
        pregunta = db.query(Pregunta).filter(Pregunta.id_pregunta == resp.id_pregunta).first()
        opcion   = db.query(Opcion).filter(Opcion.id_opcion == resp.id_opcion).first()

        if not pregunta or not opcion:
            continue

        es_correcta = bool(opcion.es_correcta)
        if es_correcta:
            correctas += 1

        # Todas las opciones de esta pregunta para mostrar en resultado
        todas_opciones = db.query(Opcion).filter(Opcion.id_pregunta == resp.id_pregunta).all()

        detalles.append({
            "id_pregunta":       pregunta.id_pregunta,
            "contenido":         pregunta.contenido,
            "id_opcion_elegida": opcion.id_opcion,
            "respuesta_elegida": opcion.respuesta,
            "es_correcta":       es_correcta,
            "opciones": [
                {
                    "id_opcion":   o.id_opcion,
                    "respuesta":   o.respuesta,
                    "es_correcta": o.es_correcta,
                }
                for o in todas_opciones
            ]
        })

    # 4 — Calcular calificación sobre 10
    calificacion = round((correctas / total) * 10, 2) if total > 0 else 0.0
    porcentaje   = round((correctas / total) * 100, 2) if total > 0 else 0.0

    # 5 — Guardar intento
    nuevo_intento = Intento(
        calificacion = calificacion,
        fecha        = datetime.utcnow(),
        id_usuario   = submit_in.id_usuario,
        id_examen    = submit_in.id_examen,
    )
    db.add(nuevo_intento)
    db.flush()  # para obtener el id_intento antes del commit

    # 6 — Guardar respuestas individuales en tabla intermedia
    for resp in submit_in.respuestas:
        opcion = db.query(Opcion).filter(Opcion.id_opcion == resp.id_opcion).first()
        if opcion:
            db.execute(
                respuesta_intento.insert().values(
                    id_intento  = nuevo_intento.id_intento,
                    id_pregunta = resp.id_pregunta,
                    id_opcion   = resp.id_opcion,
                    es_correcta = bool(opcion.es_correcta),
                )
            )

    db.commit()

    # 7 — Devolver resultado completo
    return {
        "id_intento":     nuevo_intento.id_intento,
        "id_examen":      examen.id_examen,
        "titulo_examen":  examen.titulo,
        "calificacion":   calificacion,
        "correctas":      correctas,
        "total":          total,
        "porcentaje":     porcentaje,
        "preguntas":      detalles,
    }



@router.put("/{examen_id}", response_model=Examen,  dependencies=[Depends(solo_admin)] )
def update_examen(
    examen_id: int, 
    examen_in: ExamenUpdate, 
    db: Session = Depends(get_db),

):
    """Actualiza un examen existente."""
    examen = crud_examen.update_examen(db, examen_id=examen_id, examen_in=examen_in)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")
    return examen


@router.delete("/{examen_id}", response_model=Examen,  dependencies=[Depends(solo_admin)])
def delete_examen(examen_id: int, db: Session = Depends(get_db)):
    """Elimina un examen."""
    examen = crud_examen.delete_examen(db, examen_id=examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")
    return examen