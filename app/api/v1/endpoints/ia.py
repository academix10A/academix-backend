from datetime import datetime, timedelta
import json

import httpx
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload

from app.api.deps import get_db, get_current_active_user
from app.models.usuario import Usuario
from app.models.usuario_membresia import UsuarioMembresia
from app.models.ia_consulta import IAConsulta

router = APIRouter(prefix="/ia", tags=["IA"])

WEBHOOK_IA = "https://n8n-n8n-academix.wulckn.easypanel.host/webhook/ai-academix"

MEMBRESIAS_PREMIUM = {
    "Plan Premium Mensual",
    "Plan Premium Semestral",
    "Plan Premium Anual",
}

MEMBRESIA_GRATIS = "Plan Gratuito"
LIMITE_DIARIO_GRATIS = 20


class IAConsultaIn(BaseModel):
    texto_seleccionado: str
    pregunta_seguimiento: str | None = None


def get_membresia_activa(user: Usuario):
    activas = [
        m for m in user.membresias
        if m.activa and m.membresia
    ]
    if not activas:
        return None

    activas.sort(key=lambda x: x.fecha_inicio or datetime.min, reverse=True)
    return activas[0].membresia


def get_limite_diario(nombre_membresia: str | None):
    if nombre_membresia == MEMBRESIA_GRATIS:
        return LIMITE_DIARIO_GRATIS
    if nombre_membresia in MEMBRESIAS_PREMIUM:
        return None
    return 0


def contar_consultas_hoy(db: Session, id_usuario: int) -> int:
    inicio = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    fin = inicio + timedelta(days=1)

    return (
        db.query(func.count(IAConsulta.id_ia_consulta))
        .filter(
            IAConsulta.id_usuario == id_usuario,
            IAConsulta.fecha_consulta >= inicio,
            IAConsulta.fecha_consulta < fin,
            IAConsulta.estado == "ok",
        )
        .scalar()
        or 0
    )


@router.get("/cuota")
def obtener_cuota_ia(
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user),
):
    membresia = get_membresia_activa(current_user)
    nombre = membresia.nombre if membresia else None
    limite = get_limite_diario(nombre)
    usadas = contar_consultas_hoy(db, current_user.id_usuario)

    if limite is None:
        restantes = None
    else:
        restantes = max(limite - usadas, 0)

    return {
        "membresia": nombre,
        "limite_diario": limite,
        "usadas_hoy": usadas,
        "restantes": restantes,
        "bloqueado": limite is not None and usadas >= limite,
    }


@router.post("/consultar")
async def consultar_ia(
    payload: IAConsultaIn,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user),
):
    membresia = get_membresia_activa(current_user)
    nombre = membresia.nombre if membresia else None
    limite = get_limite_diario(nombre)
    usadas = contar_consultas_hoy(db, current_user.id_usuario)

    if limite is not None and usadas >= limite:
        raise HTTPException(
            status_code=403,
            detail={
                "message": f"Agotaste tus {limite} consultas diarias de IA.",
                "membresia": nombre,
                "limite_diario": limite,
                "usadas_hoy": usadas,
                "restantes": 0,
                "bloqueado": True,
            },
        )

    body = {
        "texto_seleccionado": payload.texto_seleccionado,
    }

    if payload.pregunta_seguimiento:
        body["pregunta_seguimiento"] = payload.pregunta_seguimiento

    try:
        async with httpx.AsyncClient(timeout=90) as client:
            res = await client.post(WEBHOOK_IA, json=body)
            res.raise_for_status()

        raw = res.text
        try:
            data = res.json()
        except Exception:
            data = {
                "explicacion": raw,
                "sugerencias": []
            }

        registro = IAConsulta(
            id_usuario=current_user.id_usuario,
            id_membresia=membresia.id_membresia if membresia else None,
            texto_seleccionado=payload.texto_seleccionado,
            pregunta_seguimiento=payload.pregunta_seguimiento,
            estado="ok",
        )
        db.add(registro)
        db.commit()

        usadas_nuevas = usadas + 1
        restantes = None if limite is None else max(limite - usadas_nuevas, 0)

        data["cuota"] = {
            "membresia": nombre,
            "limite_diario": limite,
            "usadas_hoy": usadas_nuevas,
            "restantes": restantes,
            "bloqueado": limite is not None and usadas_nuevas >= limite,
        }

        return data

    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="No se pudo consultar la IA en este momento.")