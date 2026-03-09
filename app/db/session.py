from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from app.core.config import settings
from app.db.base_class import Base


# Motor de base de datos para MySQL
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Verifica que la conexión esté viva antes de usarla
    pool_recycle=3600,   # Recicla conexiones cada hora (evita timeout de MySQL)
    pool_size=5,         # Número de conexiones en el pool
    max_overflow=10,     # Conexiones extra permitidas si el pool se llena
)

# Factoría de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    """
    Crea una nueva sesión de base de datos para cada petición y 
    la cierra una vez que la petición termina.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db() -> None:
    """Inicializa la base de datos creando las tablas si no existen."""
    from app.models.intermedias import usuario_recurso, recurso_etiqueta, tema_subtema
    
    # Tablas sin dependencias (catálogos)
    from app.models.rol import Rol
    from app.models.tipo import Tipo
    from app.models.estado import Estado
    from app.models.tema import Tema
    
    # Tablas con dependencias nivel 1
    from app.models.subtema import Subtema
    from app.models.usuario import Usuario
    from app.models.etiqueta import Etiqueta  # ← ESTE ES IMPORTANTE
    
    # Tablas con dependencias nivel 2
    from app.models.recurso import Recurso
    from app.models.examen import Examen
    
    # Tablas con dependencias nivel 3
    from app.models.nota import Nota
    from app.models.publicacion import Publicacion
    from app.models.pregunta import Pregunta
    from app.models.intento import Intento
    
    # Tablas con dependencias nivel 4
    from app.models.opcion import Opcion
    from app.models.usuario_membresia import UsuarioMembresia
    from app.models.membresia import Membresia
    
    # Ahora sí crear todas las tablas
    Base.metadata.create_all(bind=engine)