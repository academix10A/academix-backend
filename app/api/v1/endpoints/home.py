# home.py
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db, get_current_active_user
from app.models.usuario import Usuario
from app.models.intento import Intento
from app.models.examen import Examen
from app.models.vista_contenido import VistaContenido
from app.models.recurso import Recurso
from app.models.publicacion import Publicacion
from app.models.progreso_contenido import ProgresoContenido

router = APIRouter(prefix="/home", tags=["Home"])

@router.get("/usuario/progreso-examenes")
def obtener_progreso_examenes_usuario(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene el progreso de exámenes del usuario actual."""
    # Obtener intentos del usuario
    intentos = db.query(Intento).filter(
        Intento.id_usuario == current_user.id_usuario
    ).order_by(Intento.fecha.desc()).offset(skip).limit(limit).all()
    
    # Calcular estadísticas
    total_intentos = len(intentos)
    promedio_calificacion = 0.0
    exames_completados = set()
    
    if total_intentos > 0:
        suma_calificaciones = sum(i.calificacion for i in intentos)
        promedio_calificacion = round(suma_calificaciones / total_intentos, 2)
        exames_completados = {i.id_examen for i in intentos}
    
    # Obtener info de los exámenes intentados
    examenes_info = []
    for intento in intentos:
        examen = db.query(Examen).filter(Examen.id_examen == intento.id_examen).first()
        if examen:
            examenes_info.append({
                "id_examen": examen.id_examen,
                "titulo": examen.titulo,
                "calificacion": intento.calificacion,
                "fecha": intento.fecha.isoformat() if intento.fecha else None
            })
    
    return {
        "total_examenes_realizados": total_intentos,
        "examenes_completados": len(exames_completados),
        "promedio_calificacion": promedio_calificacion,
        "examenes": examenes_info
    }

@router.get("/usuario/recientes")
def obtener_contenido_reciente(
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene el contenido visto recientemente por el usuario."""
    vistas = db.query(VistaContenido).filter(
        VistaContenido.id_usuario == current_user.id_usuario
    ).order_by(VistaContenido.fecha_vista.desc()).limit(limit).all()
    
    resultados = []
    for vista in vistas:
        item = {
            "id_vista": vista.id_vista,
            "fecha_vista": vista.fecha_vista.isoformat() if vista.fecha_vista else None,
            "tipo": None,
            "id": None,
            "titulo": None,
            "descripcion": None
        }
        
        if vista.id_recurso:
            recurso = db.query(Recurso).filter(Recurso.id_recurso == vista.id_recurso).first()
            if recurso:
                item["tipo"] = "recurso"
                item["id"] = recurso.id_recurso
                item["titulo"] = recurso.titulo
                item["descripcion"] = recurso.descripcion
        
        elif vista.id_publicacion:
            publicacion = db.query(Publicacion).filter(Publicacion.id_publicacion == vista.id_publicacion).first()
            if publicacion:
                item["tipo"] = "publicacion"
                item["id"] = publicacion.id_publicacion
                item["titulo"] = publicacion.titulo
                item["descripcion"] = publicacion.descripcion
        
        resultados.append(item)
    
    return resultados

@router.get("/usuario/recursos-leidos")
def obtener_recursos_leidos_usuario(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    """Obtiene los recursos leídos por el usuario con su progreso."""
    # Obtener recursos vistos
    vistas = db.query(VistaContenido).filter(
        VistaContenido.id_usuario == current_user.id_usuario,
        VistaContenido.id_recurso.isnot(None)
    ).order_by(VistaContenido.fecha_vista.desc()).offset(skip).limit(limit).all()
    
    resultados = []
    for vista in vistas:
        if not vista.id_recurso:
            continue
            
        recurso = db.query(Recurso).filter(Recurso.id_recurso == vista.id_recurso).first()
        if not recurso:
            continue
        
        # Obtener progreso
        progreso = db.query(ProgresoContenido).filter(
            ProgresoContenido.id_usuario == current_user.id_usuario,
            ProgresoContenido.id_recurso == vista.id_recurso
        ).first()
        
        resultados.append({
            "id_recurso": recurso.id_recurso,
            "titulo": recurso.titulo,
            "descripcion": recurso.descripcion,
            "fecha_vista": vista.fecha_vista.isoformat() if vista.fecha_vista else None,
            "porcentaje_leido": progreso.porcentaje_leido if progreso else 0,
            "completado": progreso.completado if progreso else False
        })
    
    return resultados

