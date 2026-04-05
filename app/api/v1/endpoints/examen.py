# examen.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.api.deps import get_db, get_current_active_user
from app.crud import crud_examen
from app.schemas.examen import (
    Examen, ExamenCreate, ExamenUpdate,
    ExamenCompleto, ExamenSubmit, ExamenResultado, ExamenRealizado, ExamenRealizadoDetalle
)
from app.core.permissions import PermissionChecker, Beneficios, has_benefit, is_admin
from app.models.pregunta import Pregunta
from app.models.opcion import Opcion
from app.models.intento import Intento
from app.models.usuario import Usuario
from app.models.intermedias import respuesta_intento

router = APIRouter(prefix="/examen", tags=["Examenes"])

solo_admin      = PermissionChecker(roles=["admin"])
puede_historial = PermissionChecker(beneficios=[Beneficios.HISTORIAL])
puede_desglose = PermissionChecker(beneficios=[Beneficios.DESGLOSE])

def _verificar_acceso_examen(examen, current_user: Usuario):
    """
    Lanza 403 si el usuario no puede ver el examen según su dificultad.
    - Sin ningún beneficio de examen → 403
    - Freemium (solo básicos) intentando ver avanzado → 403
    - Premium (avanzados) → pasa siempre
    - Admin → pasa siempre (manejado en PermissionChecker)
    """
    tiene_basicos   = has_benefit(current_user, Beneficios.EXAMENES_BASICOS)
    tiene_avanzados = has_benefit(current_user, Beneficios.EXAMENES_AVANZADOS)

    if is_admin(current_user):
        return

    if not tiene_basicos and not tiene_avanzados:
        raise HTTPException(status_code=403, detail="No tienes acceso a exámenes")

    nivel = (examen.subtema.nivel_dificultad or "").lower().strip()
    if nivel != "basico" and not tiene_avanzados:
        raise HTTPException(status_code=403, detail="No tienes acceso a este examen avanzado")

@router.get("/", response_model=List[Examen])
def list_examen(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """
    Lista exámenes según el plan del usuario:
    - Admin / Premium (avanzados): ve todos, incluyendo los ya contestados.
    - Freemium (solo básicos): ve solo básicos y EXCLUYE los que ya contestó.
    - Sin beneficio: 403.
    """
    tiene_avanzados = has_benefit(current_user, Beneficios.EXAMENES_AVANZADOS)
    tiene_basicos   = has_benefit(current_user, Beneficios.EXAMENES_BASICOS)

    if is_admin(current_user) or tiene_avanzados:
        # Ve todo, sin excluir realizados
        return crud_examen.get_examenes_filtrados(
            db, solo_basicos=False, skip=skip, limit=limit
        )

    if tiene_basicos:
        # Solo básicos + excluir los ya contestados
        return crud_examen.get_examenes_filtrados(
            db,
            solo_basicos=True,
            skip=skip,
            limit=limit,
            excluir_realizados_por=current_user.id_usuario
        )

    raise HTTPException(status_code=403, detail="No tienes acceso a exámenes")

@router.get("/{examen_id}", response_model=Examen)
def read_examen(
    examen_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene un examen por ID. Verifica acceso según dificultad."""
    examen = crud_examen.get_examen(db, examen_id=examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")

    _verificar_acceso_examen(examen, current_user)
    return examen

@router.get("/titulo/{titulo}", response_model=Examen)
def get_examen_by_titulo(
    titulo: str,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene un examen por título. Verifica acceso según dificultad."""
    examen = crud_examen.get_examen_by_titulo(db, titulo=titulo)
    if not examen:
        raise HTTPException(status_code=404, detail=f"Examen '{titulo}' no encontrado")

    _verificar_acceso_examen(examen, current_user)
    return examen

@router.get("/{examen_id}/completo", response_model=ExamenCompleto)
def get_examen_completo(
    examen_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """
    Devuelve el examen con todas sus preguntas y opciones.
    Las opciones NO incluyen es_correcta para evitar trampa.
    Verifica acceso según dificultad.
    """
    examen = crud_examen.get_examen(db, examen_id=examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")

    _verificar_acceso_examen(examen, current_user)

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

@router.post("/", response_model=Examen, status_code=201, dependencies=[Depends(solo_admin)])
def create_examen(examen_in: ExamenCreate, db: Session = Depends(get_db)):
    """Crea un nuevo examen."""
    if crud_examen.get_examen_by_titulo(db, titulo=examen_in.titulo):
        raise HTTPException(status_code=400, detail="Ya existe un examen con ese titulo")
    return crud_examen.create_examen(db, examen_in=examen_in)

@router.post("/submit", response_model=ExamenResultado, dependencies=[Depends(PermissionChecker(
    beneficios=[Beneficios.EXAMENES_BASICOS, Beneficios.EXAMENES_AVANZADOS]
))])
def submit_examen(
    submit_in: ExamenSubmit,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """
    Recibe las respuestas del usuario, calcula la calificación y guarda el intento.

    - Usuarios con INTENTOS_ILIMITADOS pueden repetir sin límite.
    - Usuarios con INTENTOS_LIMITADOS tienen máximo 2 intentos.
    - Freemium sin beneficio de intentos: solo 1 intento.
    - El resultado devuelto depende del beneficio:
        · DESGLOSE → calificación + detalle completo.
        · Sin desglose → solo calificación.
    """
    # 1 — Validar que el examen existe y el usuario tiene acceso
    examen = crud_examen.get_examen(db, examen_id=submit_in.id_examen)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")

    _verificar_acceso_examen(examen, current_user)

    # 2 — Validar intentos según beneficio del usuario
    intentos_count = db.query(Intento).filter(
        Intento.id_usuario == current_user.id_usuario,
        Intento.id_examen  == submit_in.id_examen
    ).count()

    if has_benefit(current_user, Beneficios.INTENTOS_ILIMITADOS):
        pass  # Sin límite

    elif has_benefit(current_user, Beneficios.INTENTOS_LIMITADOS):
        if intentos_count >= 2:
            raise HTTPException(
                status_code=400,
                detail="Has alcanzado el límite de 2 intentos para este examen."
            )

    else:
        # Sin beneficio explícito de intentos → 1 solo intento
        if intentos_count >= 1:
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

    # 4 — Calcular calificación
    calificacion = round((correctas / total) * 10, 2) if total > 0 else 0.0
    porcentaje   = round((correctas / total) * 100, 2) if total > 0 else 0.0

    # 5 — Guardar intento
    nuevo_intento = Intento(
        calificacion = calificacion,
        fecha        = datetime.utcnow(),
        id_usuario   = current_user.id_usuario,
        id_examen    = submit_in.id_examen,
    )
    db.add(nuevo_intento)
    db.flush()

    # 6 — Guardar respuestas individuales
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

    # 7 — Devolver resultado según beneficio
    resultado_base = {
        "id_intento":    nuevo_intento.id_intento,
        "id_examen":     examen.id_examen,
        "titulo_examen": examen.titulo,
        "calificacion":  calificacion,
        "correctas":     correctas,
        "total":         total,
        "porcentaje":    porcentaje,
    }

    if has_benefit(current_user, Beneficios.DESGLOSE):
        return {**resultado_base, "preguntas": detalles}

    return {**resultado_base, "preguntas": []}

@router.get("/{examen_id}/mis-intentos", dependencies=[Depends(puede_historial)])
def get_mis_intentos_examen(
    examen_id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """
    Devuelve todos los intentos del usuario en un examen específico.
    Solo disponible para usuarios con beneficio HISTORIAL (premium).
    Incluye calificación, fecha y posición (intento 1, 2, 3...).
    """
    examen = crud_examen.get_examen(db, examen_id=examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")

    _verificar_acceso_examen(examen, current_user)

    intentos = crud_examen.get_intentos_por_examen(
        db,
        id_usuario=current_user.id_usuario,
        id_examen=examen_id
    )

    if not intentos:
        raise HTTPException(status_code=404, detail="No tienes intentos en este examen")

    return {
        "id_examen":     examen.id_examen,
        "titulo_examen": examen.titulo,
        "total_intentos": len(intentos),
        "intentos": [
            {
                "numero_intento": idx + 1,
                "id_intento":     intento.id_intento,
                "calificacion":   intento.calificacion,
                "fecha":          intento.fecha,
            }
            for idx, intento in enumerate(reversed(intentos))  # orden cronológico
        ]
    }

@router.get(
    "/usuario/{id_usuario}/detalles",
    response_model=List[ExamenRealizadoDetalle],
    dependencies=[Depends(puede_desglose)]   # 403 si no tiene DESGLOSE
)
def get_examenes_realizados_detalle(
    id_usuario: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user),
):
    """
    Devuelve exámenes realizados con desglose completo:
    respuestas correctas, total, porcentaje y si aprobó.
    Requiere beneficio DESGLOSE.
    """
    return crud_examen.get_examenes_realizados_detalle(db, id_usuario)

@router.get("/usuario/{id_usuario}/realizados", response_model=List[ExamenRealizado], dependencies=[Depends(puede_historial)])
def get_examenes_realizados(id_usuario: int, db: Session = Depends(get_db)):
    """Devuelve todos los exámenes realizados por un usuario."""
    return crud_examen.get_examenes_realizados_por_usuario(db, id_usuario)

@router.put("/{examen_id}", response_model=Examen, dependencies=[Depends(solo_admin)])
def update_examen(examen_id: int, examen_in: ExamenUpdate, db: Session = Depends(get_db)):
    """Actualiza un examen existente."""
    examen = crud_examen.update_examen(db, examen_id=examen_id, examen_in=examen_in)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")
    return examen

@router.delete("/{examen_id}", response_model=Examen, dependencies=[Depends(solo_admin)])
def delete_examen(examen_id: int, db: Session = Depends(get_db)):
    """Elimina un examen."""
    examen = crud_examen.delete_examen(db, examen_id=examen_id)
    if not examen:
        raise HTTPException(status_code=404, detail="Examen no encontrado")
    return examen
