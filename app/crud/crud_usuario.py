
from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from app.core.security import get_password_hash, verify_password
from app.models.usuario import Usuario
from app.models.rol import Rol
from app.models.estado import Estado
from app.models.membresia import Membresia
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate

def get_usuario(db: Session, usuario_id: int) -> Optional[Usuario]:
    if usuario_id <= 0:
        return None
    
    return db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()


def get_usuario_by_nombre(db: Session, nombre: str) -> Optional[Usuario]:
    
    if not nombre or not nombre.strip():
        return None
    
    return db.query(Usuario).filter(Usuario.nombre == nombre.strip()).first()


def get_usuario_by_correo(db: Session, correo: str) -> Optional[Usuario]:
    if not correo or not correo.strip():
        return None
    
    # Normalizar correo a minúsculas
    correo_normalizado = correo.lower().strip()
    
    return db.query(Usuario).filter(Usuario.correo == correo_normalizado).first()


def get_usuarios(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    id_estado: Optional[int] = None,
    id_rol: Optional[int] = None,
    id_membresia: Optional[int] = None
) -> List[Usuario]:
    if skip < 0:
        skip = 0
    if limit <= 0 or limit > 1000:  # Máximo 1000 para evitar sobrecarga
        limit = 100
    
    query = db.query(Usuario)
    
    # Aplicar filtros opcionales
    if id_estado and id_estado > 0:
        query = query.filter(Usuario.id_estado == id_estado)
    
    if id_rol and id_rol > 0:
        query = query.filter(Usuario.id_rol == id_rol)
        
    if id_membresia and id_membresia > 0:
        query = query.filter(Usuario.id_membresia == id_membresia)
    
    return query.offset(skip).limit(limit).all()


def count_usuarios(
    db: Session,
    id_estado: Optional[int] = None,
    id_rol: Optional[int] = None ,
    id_membresia: Optional[int] = None
) -> int:
    """
    Cuenta el total de usuarios con filtros opcionales.
    
    Útil para paginación en el frontend.
    """
    query = db.query(Usuario)
    
    if id_estado and id_estado > 0:
        query = query.filter(Usuario.estado == id_estado)
    
    if id_rol and id_rol > 0:
        query = query.filter(Usuario.id_rol == id_rol)
    
    if id_membresia and id_membresia > 0:
        query = query.filter(Usuario.id_membresia == id_membresia)
    
    return query.count()

def _validar_rol_existe(db: Session, id_rol: int) -> None:
    rol = db.query(Rol).filter(Rol.id_rol == id_rol).first()
    if not rol:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El rol con ID {id_rol} no existe"
        )

def _validar_estado_existe(db: Session, id_estado: int) -> None:
    """Valida que el estado exista en la BD."""
    estado = db.query(Estado).filter(Estado.id_estado == id_estado).first()
    if not estado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El estado con ID {id_estado} no existe"
        )
def _validar_membresia_existe(db: Session, id_membresia: int) -> None:
    """Valida que la membresia exista en la BD."""
    membresia = db.query(Membresia).filter(Membresia.id_membresia == id_membresia).first()
    if not membresia:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El estado con ID {id_membresia} no existe"
        )

def _validar_correo_unico(db: Session, correo: str, usuario_id: Optional[int] = None) -> None:
    correo_normalizado = correo.lower().strip()
    
    query = db.query(Usuario).filter(Usuario.correo == correo_normalizado)
    
    # Si es update, ignorar el propio usuario
    if usuario_id:
        query = query.filter(Usuario.id_usuario != usuario_id)
    
    usuario_existente = query.first()
    
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un usuario con ese correo electrónico"
        )

def create_usuario(db: Session, usuario_in: UsuarioCreate) -> Usuario:

    _validar_rol_existe(db, usuario_in.id_rol)
    
    id_membresia = usuario_in.id_membresia or 1 
    _validar_membresia_existe(db, id_membresia)
    
    _validar_correo_unico(db, usuario_in.correo)

    id_estado = usuario_in.id_estado or 1  # default = 1 (activo)
    _validar_estado_existe(db, id_estado)
    
    contrasena_hash = get_password_hash(usuario_in.contrasena)

    db_obj = Usuario(
        nombre=usuario_in.nombre,
        apellido_paterno=usuario_in.apellido_paterno,
        apellido_materno=usuario_in.apellido_materno,
        correo=usuario_in.correo.lower().strip(),  
        contrasena_hash=contrasena_hash,
        id_rol=usuario_in.id_rol,
        id_estado=id_estado,
        id_membresia=id_membresia
    )
    
    try:
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    except IntegrityError as e:
        db.rollback()
        # Capturar errores de integridad (unique, foreign key, etc.)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error de integridad en la base de datos. Verifica los datos."
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al crear el usuario"
        )

def update_usuario(
    db: Session, 
    usuario_id: int, 
    usuario_in: UsuarioUpdate
) -> Optional[Usuario]:

    db_obj = get_usuario(db, usuario_id=usuario_id)
    if not db_obj:
        return None
    
    
    update_data = usuario_in.model_dump(exclude_unset=True)
    
    if "id_rol" in update_data and update_data["id_rol"]:
        _validar_rol_existe(db, update_data["id_rol"])
    
    
    if "correo" in update_data and update_data["correo"]:
        _validar_correo_unico(db, update_data["correo"], usuario_id=usuario_id)
        # Normalizar correo
        update_data["correo"] = update_data["correo"].lower().strip()
    
    
    if "id_estado" in update_data and update_data["id_estado"]:
        _validar_estado_existe(db, update_data["id_estado"])
    
    if "id_membresia" in update_data and update_data["id_menbresia"]:
        _validar_membresia_existe(db, update_data["id_membresia"])
    
    if "contrasena" in update_data and update_data["contrasena"]:
        # Hashear nueva contraseña
        update_data["contrasena_hash"] = get_password_hash(update_data["contrasena"])
        # Eliminar contraseña plana del dict
        del update_data["contrasena"]
    
    # 4. Aplicar cambios
    try:
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error de integridad al actualizar el usuario"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al actualizar el usuario"
        )


def soft_delete_usuario(db: Session, usuario_id: int) -> Optional[Usuario]:

    db_obj = get_usuario(db, usuario_id=usuario_id)
    if not db_obj:
        return None
    
    estado_inactivo = db.query(Estado).filter(Estado.nombre == "inactivo").first()
    if not estado_inactivo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El estado 'inactivo' no existe"
        )
    db_obj.id_estado = estado_inactivo.id_estado 
    
    try:
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al desactivar el usuario"
        )

def is_active(user: Usuario) -> bool:

    return user.estado.nombre == "activo" if user.estado else False



def authenticate(db: Session, correo: str, password: str) -> Optional[Usuario]:

    # Normalizar correo
    correo_normalizado = correo.lower().strip()
    
    user = get_usuario_by_correo(db, correo=correo_normalizado)
    if not user:
        return None
    
    if not verify_password(password, user.contrasena_hash):
        return None
    
    return user



def usuario_puede_actualizar_perfil(usuario_actual: Usuario, usuario_id_objetivo: int) -> bool:

    return usuario_actual.id_usuario == usuario_id_objetivo


def cambiar_contrasena(
    db: Session,
    usuario_id: int,
    contrasena_actual: str,
    contrasena_nueva: str
) -> Usuario:

    usuario = get_usuario(db, usuario_id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    
    # Verificar contraseña actual
    if not verify_password(contrasena_actual, usuario.contrasena_hash):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Contraseña actual incorrecta"
        )
    
    # Actualizar contraseña
    usuario.contrasena_hash = get_password_hash(contrasena_nueva)
    
    try:
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al cambiar la contraseña"
        )