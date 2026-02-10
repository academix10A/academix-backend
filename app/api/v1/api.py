from fastapi import APIRouter

from app.api.v1.endpoints import auth, tema, recursos, usuarios, examen, subtema, estado, rol, tipo, etiqueta, publicaciones, nota, pregunta, opcion, intento

api_router = APIRouter()
api_router.include_router(auth.router, tags=["Auth"])
api_router.include_router(publicaciones.router, prefix="/publicacion", tags=["Publicaciones"])
api_router.include_router(tema.router, prefix="/tema", tags=["Tema"])
api_router.include_router(nota.router, prefix="/nota", tags=["Notas"])
api_router.include_router(subtema.router, prefix="/subtema", tags=["Subtemas"])
api_router.include_router(recursos.router, prefix="/recursos", tags=["Recursos"])
api_router.include_router(estado.router, prefix="/estado", tags=["Estados"])
api_router.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
api_router.include_router(examen.router, prefix="/examenes", tags=["Examenes"])
api_router.include_router(pregunta.router, prefix="/pregunta", tags=["Preguntas"])
api_router.include_router(opcion.router, prefix="/opcion", tags=["Opciones"])
api_router.include_router(intento.router, prefix="/intento", tags=["Intentos"])
api_router.include_router(rol.router, prefix="/rol", tags=["Roles"])
api_router.include_router(tipo.router, prefix="/tipo", tags=["Tipos"])
api_router.include_router(etiqueta.router, prefix="/etiqueta", tags=["Etiquetas"])

