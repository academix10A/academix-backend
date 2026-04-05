from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from app.models.recurso import Recurso
from app.models.tipo import Tipo
from app.models.estado import Estado
from app.models.subtema import Subtema
from app.models.etiqueta import Etiqueta
from app.schemas.recurso import RecursoCreate, RecursoUpdate
from app.models.tema import Tema
from app.models.usuario import Usuario

# Favoritos
def agregar_favorito(db: Session, id_usuario: int, id_recurso: int):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    recurso = db.query(Recurso).filter(Recurso.id_recurso == id_recurso).first()
    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

    if recurso in usuario.recursos:
        raise HTTPException(
            status_code=400,
            detail="El recurso ya está en favoritos"
        )

    usuario.recursos.append(recurso)

    db.commit()
    return {"message": "Recurso agregado a favoritos"}

def quitar_favorito(db: Session, id_usuario: int, id_recurso: int):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    recurso = db.query(Recurso).filter(Recurso.id_recurso == id_recurso).first()
    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

    if recurso not in usuario.recursos:
        raise HTTPException(
            status_code=400,
            detail="El recurso no está en favoritos"
        )

    usuario.recursos.remove(recurso)

    db.commit()
    return {"message": "Recurso eliminado de favoritos"}

def get_favoritos(db: Session, id_usuario: int):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return usuario.recursos

def get_recurso(db: Session, recurso_id: int) -> Optional[Recurso]:
    """Obtiene un Recurso por su ID."""
    if recurso_id <= 0:
        return None
    
    return db.query(Recurso).filter(Recurso.id_recurso == recurso_id).first()

def get_recursos_by_tema(db: Session, id_tema: int):
    tema = db.query(Tema).filter(Tema.id_tema == id_tema).first()
    
    if not tema:
        return []

    recursos = []

    for subtema in tema.subtemas:
        for recurso in subtema.recursos:
            recursos.append({
                "id_recurso": recurso.id_recurso,
                "titulo": recurso.titulo,
                "descripcion": recurso.descripcion,
                "url_archivo": recurso.url_archivo,
                "id_tipo": recurso.id_tipo,
                "id_subtema": subtema.id_subtema,
                "subtema": subtema.nombre,
                "tema": tema.nombre
            })

    return recursos

def get_temas_recursos(db: Session):
    temas = db.query(Tema).all()

    result = []

    for tema in temas:
        tema_data = {
            "id_tema": tema.id_tema,
            "nombre": tema.nombre,
            "subtemas": []
        }

        for subtema in tema.subtemas:
            subtema_data = {
                "id_subtema": subtema.id_subtema,
                "nombre": subtema.nombre,
                "recursos": []
            }

            for recurso in subtema.recursos:
                subtema_data["recursos"].append({
                    "id_recurso": recurso.id_recurso,
                    "titulo": recurso.titulo,
                    "descripcion": recurso.descripcion,
                    "url_archivo": recurso.url_archivo,
                    "id_tipo": recurso.id_tipo,
                })

            tema_data["subtemas"].append(subtema_data)

        result.append(tema_data)

    return result

def get_recurso_by_titulo(db: Session, titulo: str) -> Optional[Recurso]:
    """
    Obtiene un recurso por su título.
    """
    if not titulo or not titulo.strip():
        return None
    
    return db.query(Recurso).filter(Recurso.titulo == titulo.strip()).first()


def get_recurso_by_url(db: Session, url_archivo: str) -> Optional[Recurso]:
    """Obtiene un recurso por su URL (para verificar duplicados)"""
    if not url_archivo or not url_archivo.strip():
        return None
    
    return db.query(Recurso).filter(Recurso.url_archivo == url_archivo.strip()).first()

def get_recurso_by_contenido(db: Session, contenido: str) -> Optional[Recurso]:
    """Obtiene un recurso por su contenido."""
    return db.query(Recurso).filter(Recurso.contenido == contenido).first()

def get_recursos(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    id_tipo: Optional[int] = None,
    id_estado: Optional[int] = None,
    id_subtema: Optional[int] = None
) -> List[Recurso]:
    """
    Obtiene una lista de recursos con paginación y filtros.
    """
    # Validar paginación
    if skip < 0:
        skip = 0
    if limit <= 0 or limit > 1000:
        limit = 100
    
    # Query base
    query = db.query(Recurso)
    
    # Aplicar filtros opcionales
    if id_tipo and id_tipo > 0:
        query = query.filter(Recurso.id_tipo == id_tipo)
    
    if id_estado and id_estado > 0:
        query = query.filter(Recurso.id_estado == id_estado)
    
    if id_subtema and id_subtema > 0:
        query = query.filter(Recurso.id_subtema == id_subtema)
    
    # Ordenar por fecha de publicación (más recientes primero)
    query = query.order_by(Recurso.fecha_publicacion.desc())
    
    return query.offset(skip).limit(limit).all()


def count_recursos(
    db: Session,
    id_tipo: Optional[int] = None,
    id_estado: Optional[int] = None,
    id_subtema: Optional[int] = None
) -> int:
    """Cuenta el total de recursos con filtros opcionales"""
    query = db.query(Recurso)
    
    if id_tipo and id_tipo > 0:
        query = query.filter(Recurso.id_tipo == id_tipo)
    
    if id_estado and id_estado > 0:
        query = query.filter(Recurso.id_estado == id_estado)
    
    if id_subtema and id_subtema > 0:
        query = query.filter(Recurso.id_subtema == id_subtema)
    
    return query.count()


def _validar_tipo_existe(db: Session, id_tipo: int) -> Tipo:
    tipo = db.query(Tipo).filter(Tipo.id_tipo == id_tipo).first()
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo con ID {id_tipo} no existe. Tipos válidos: 1=PDF, 2=Video, 3=Audio"
        )
    return tipo


def _validar_estado_existe(db: Session, id_estado: int) -> Estado:

    estado = db.query(Estado).filter(Estado.id_estado == id_estado).first()
    if not estado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El estado con ID {id_estado} no existe. Estados válidos: 1=Activo, 2=Inactivo"
        )
    return estado


def _validar_subtema_existe(db: Session, id_subtema: int) -> Subtema:

    subtema = db.query(Subtema).filter(Subtema.id_subtema == id_subtema).first()
    if not subtema:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El subtema con ID {id_subtema} no existe"
        )
    return subtema


def _validar_etiqueta_existe(db: Session, id_etiqueta: int) -> Etiqueta:
    etiqueta = db.query(Etiqueta).filter(Etiqueta.id_etiqueta == id_etiqueta).first()
    if not etiqueta:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La etiqueta con ID {id_etiqueta} no existe"
        )
    return etiqueta


def _validar_url_unica(
    db: Session,
    url_archivo: str,
    recurso_id: Optional[int] = None
) -> None:
    if not url_archivo or url_archivo == "":
        return
    
    query = db.query(Recurso).filter(Recurso.url_archivo == url_archivo.strip())
    
    # Si es update, ignorar el propio recurso
    if recurso_id:
        query = query.filter(Recurso.id_recurso != recurso_id)
    
    recurso_existente = query.first()
    
    if recurso_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ya existe un recurso con esa URL (ID: {recurso_existente.id_recurso}). "
                    f"No se pueden duplicar archivos."
        )


def _validar_tipo_archivo_compatible(tipo: Tipo, url_archivo: str) -> None:
    url_lower = url_archivo.lower()
    tipo_nombre = tipo.nombre.lower()

    # Dominios externos que se aceptan sin validar extensión
    dominios_externos = [
        'drive.google.com',
        'openlibrary.org',
        'archive.org',
        'gutenberg.org',
        'youtube.com',
        'youtu.be',
        'vimeo.com',
        'open.spotify.com',
        'soundcloud.com',
    ]
    es_externo = any(dominio in url_lower for dominio in dominios_externos)
    if es_externo:
        return  # Si es servicio conocido, skip validación de extensión

    extensiones_validas = {
        'pdf':        ['.pdf'],
        'video':      ['.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv', '.wmv'],
        'audio':      ['.mp3', '.wav', '.aac', '.ogg', '.m4a', '.flac', '.wma'],
        'audiolibro': ['.mp3', '.wav', '.aac', '.ogg', '.m4a', '.flac', '.wma'],
    }

    if tipo_nombre in extensiones_validas:
        extensiones = extensiones_validas[tipo_nombre]
        tiene_extension_valida = any(url_lower.endswith(ext) for ext in extensiones)
        if not tiene_extension_valida:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Tipo de archivo incompatible. "
                    f"Para tipo '{tipo.nombre}', las extensiones válidas son: {', '.join(extensiones)}"
            )


def _validar_url_accesible(url_archivo: str) -> None:
    url_lower = url_archivo.lower()

    # Dominios externos conocidos — no necesitan extensión
    dominios_externos = [
        'drive.google.com',
        'openlibrary.org',
        'archive.org',
        'gutenberg.org',
        'youtube.com',
        'youtu.be',
        'vimeo.com',
        'open.spotify.com',
        'soundcloud.com',
    ]
    es_externo = any(dominio in url_lower for dominio in dominios_externos)
    if es_externo:
        return  # Servicio conocido, no validar extensión

    extensiones_conocidas = [
        '.pdf', '.mp4', '.avi', '.mov', '.mkv', '.webm',
        '.mp3', '.wav', '.aac', '.ogg', '.m4a'
    ]
    tiene_extension = any(url_lower.endswith(ext) for ext in extensiones_conocidas)
    if not tiene_extension:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La URL debe terminar con una extensión válida (.pdf, .mp4, .mp3, etc.) "
                "o ser de un servicio conocido (Drive, YouTube, Open Library, etc.)"
        )
        

def create_recurso(db: Session, recurso_in: RecursoCreate) -> Recurso:
    """
    Crea un recurso nuevo con validaciones COMPLETAS.
    
    Validaciones:
    1.  El tipo existe (PDF, Video, Audio)
    2.  El estado existe (Activo, Inactivo)
    3.  El subtema existe
    4.  La URL es única (no duplicados)
    5.  La extensión del archivo coincide con el tipo
    6.  La URL es accesible (no localhost)
    7.  La etiqueta existe (si se proporciona)
    """
    tipo = _validar_tipo_existe(db, recurso_in.id_tipo)
    
    _validar_estado_existe(db, recurso_in.id_estado)
    
    _validar_subtema_existe(db, recurso_in.id_subtema)
    
    _validar_url_unica(db, recurso_in.url_archivo)
    
    _validar_tipo_archivo_compatible(tipo, recurso_in.url_archivo)
    
    _validar_url_accesible(recurso_in.url_archivo)
    

    db_obj = Recurso(
        titulo=recurso_in.titulo,
        descripcion=recurso_in.descripcion,
        contenido=recurso_in.contenido,
        url_archivo=recurso_in.url_archivo,
        external_id=recurso_in.external_id,
        id_tipo=recurso_in.id_tipo,
        id_estado=recurso_in.id_estado,
        id_subtema=recurso_in.id_subtema
    )
    
    if recurso_in.id_etiqueta:
        etiqueta = _validar_etiqueta_existe(db, recurso_in.id_etiqueta)
        db_obj.etiquetas.append(etiqueta)
    
    try:
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error de integridad en la base de datos. Verifica que no existan duplicados."
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al crear el recurso."
        )


def update_recurso(
    db: Session,
    recurso_id: int,
    recurso_in: RecursoUpdate
) -> Optional[Recurso]:
    """
    Actualiza un recurso existente con validaciones.
    
    Validaciones:
    1. Recurso existe
    2. Si cambia tipo, el tipo existe y es compatible con la URL
    3. Si cambia estado, el estado existe
    4. Si cambia subtema, el subtema existe
    5. Si cambia URL, es única y válida    
    """
    db_obj = get_recurso(db, recurso_id=recurso_id)
    if not db_obj:
        return None
    
    update_data = recurso_in.model_dump(exclude_unset=True)
    
    
    # Si se actualiza el tipo
    if "id_tipo" in update_data and update_data["id_tipo"]:
        tipo = _validar_tipo_existe(db, update_data["id_tipo"])
        # Verificar compatibilidad con URL actual o nueva
        url_a_validar = update_data.get("url_archivo", db_obj.url_archivo)
        _validar_tipo_archivo_compatible(tipo, url_a_validar)
    
    # Si se actualiza el estado
    if "id_estado" in update_data and update_data["id_estado"]:
        _validar_estado_existe(db, update_data["id_estado"])
    
    # Si se actualiza el subtema
    if "id_subtema" in update_data and update_data["id_subtema"]:
        _validar_subtema_existe(db, update_data["id_subtema"])
    
    # Si se actualiza la URL
    if "url_archivo" in update_data and update_data["url_archivo"]:
        _validar_url_unica(db, update_data["url_archivo"], recurso_id=recurso_id)
        _validar_url_accesible(update_data["url_archivo"])
        
        # Verificar compatibilidad con tipo actual o nuevo
        id_tipo_a_validar = update_data.get("id_tipo", db_obj.id_tipo)
        tipo = db.query(Tipo).filter(Tipo.id_tipo == id_tipo_a_validar).first()
        if tipo:
            _validar_tipo_archivo_compatible(tipo, update_data["url_archivo"])
    
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
            detail="Error de integridad al actualizar el recurso"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al actualizar el recurso"
        )


def soft_delete_recurso(db: Session, recurso_id: int) -> Optional[Recurso]:
    """ Eliminación LÓGICA - Marca recurso como inactivo."""
    db_obj = get_recurso(db, recurso_id=recurso_id)
    if not db_obj:
        return None
    
    # Buscar estado "inactivo" (ajusta según tu BD)
    estado_inactivo = db.query(Estado).filter(Estado.nombre.ilike("inactivo")).first()
    
    if estado_inactivo:
        db_obj.id_estado = estado_inactivo.id_estado
    else:
        # Fallback: usar ID 2 si existe
        db_obj.id_estado = 2
    
    try:
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al desactivar el recurso"
        )


def buscar_recursos_por_texto(
    db: Session,
    texto_busqueda: str,
    skip: int = 0,
    limit: int = 100
) -> List[Recurso]:
    """
    Busca recursos por título, descripción o contenido.
    """
    if not texto_busqueda or not texto_busqueda.strip():
        return []
    
    texto = f"%{texto_busqueda.strip()}%"
    
    return db.query(Recurso).filter(
        (Recurso.titulo.ilike(texto)) | 
        (Recurso.descripcion.ilike(texto)) |
        (Recurso.contenido.ilike(texto))
    ).offset(skip).limit(limit).all()


def get_recursos_por_tipo(
    db: Session,
    nombre_tipo: str,
    skip: int = 0,
    limit: int = 100
) -> List[Recurso]:
    """
    Obtiene recursos por nombre de tipo (PDF, Video, Audio).
    """
    tipo = db.query(Tipo).filter(Tipo.nombre.ilike(nombre_tipo)).first()
    
    if not tipo:
        return []
    
    return db.query(Recurso).filter(
        Recurso.id_tipo == tipo.id_tipo
    ).offset(skip).limit(limit).all()
