from fastapi import FastAPI
# from sqladmin import Admin
# from app.admin.views import UserAdmin
from app.db.session import init_db
from app.api.v1.api import tema, usuarios, auth, recursos,examen, subtema, estado, rol, tipo, etiqueta, publicaciones, nota, pregunta, opcion, intento

# Inicializar base de datos (crear tablas)
init_db()

app = FastAPI(
    title="Academix API",
    description="API para plataforma de biblioteca virtual y hub de estudio colaborativo",
    version="1.0.0"
)

# Configuración de Admin (descomentar cuando esté listo):
# from app.db.session import engine
# admin = Admin(app, engine)
# admin.add_view(UserAdmin)

# Incluir routers
app.include_router(auth.router, prefix="/api")
app.include_router(usuarios.router, prefix="/api")
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


@app.get("/")
def root():
    return {
        "message": "Welcome to Academix API",
        "status": "active",
        "author": "Arath",
        "version": "1.0.0"
    }