from sqlalchemy.orm import Session
from app.models.usuario_membresia import UsuarioMembresia

def get_membresia_by_usuario(db: Session, id_usuario: int):
    return db.query(UsuarioMembresia)\
        .filter(
            UsuarioMembresia.id_usuario == id_usuario,
            UsuarioMembresia.activa == True
        ).first()
def get_membresias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UsuarioMembresia).offset(skip).limit(limit).all()