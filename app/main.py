import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from sqladmin import Admin
# from app.admin.views import UserAdmin
from app.db.session import init_db
from app.api.v1.api import tema, usuarios, auth, recursos, examen, subtema, estado, rol, tipo, etiqueta, publicaciones, nota, pregunta, opcion, intento, membresia, beneficio, vistas, progreso, home, usuario_membresia, paypal, search, offline, proxy, ia

import logging
from app.db.seed import run_seed

app = FastAPI(
    title="Academix API",
    description="API para plataforma de biblioteca virtual y hub de estudio colaborativo",
    version="1.0.0",
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://192.168.152.1:3000",
        "https://academix.homes",
        "https://www.academix.homes"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router, prefix="/api")
app.include_router(usuarios.router, prefix="/api")
app.include_router(beneficio.router, prefix="/api")
app.include_router(membresia.router, prefix="/api")
app.include_router(rol.router, prefix="/api")
app.include_router(nota.router, prefix="/api")
app.include_router(publicaciones.router, prefix="/api")
app.include_router(tema.router, prefix="/api")
app.include_router(subtema.router, prefix="/api")
app.include_router(recursos.router, prefix="/api")
app.include_router(examen.router, prefix="/api")
app.include_router(pregunta.router, prefix="/api")
app.include_router(opcion.router, prefix="/api")
app.include_router(intento.router, prefix="/api")
app.include_router(estado.router, prefix="/api")
app.include_router(tipo.router, prefix="/api")
app.include_router(etiqueta.router, prefix="/api")
app.include_router(usuario_membresia.router, prefix="/api")
app.include_router(vistas.router, prefix="/api")
app.include_router(progreso.router, prefix="/api")
app.include_router(home.router, prefix="/api")
app.include_router(paypal.router, prefix="/api")
app.include_router(search.router, prefix="/api")
app.include_router(offline.router, prefix="/api")
app.include_router(proxy.router, prefix="/api")
app.include_router(ia.router, prefix="/api")
@app.on_event("startup")
def on_startup():
    if os.getenv("ENV") != "test":
        init_db()
        run_seed()


@app.get("/")
def root():
    return {
        "message": "Welcome to Academix API",
        "status": "active",
        "author": "Arath",
        "version": "1.0.0"
    }

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)