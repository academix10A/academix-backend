"""
Tablas intermedias para relaciones Many-to-Many (M:M)
"""
from sqlalchemy import Column, Integer, DateTime, Table, ForeignKey
from app.db.base_class import Base
from datetime import datetime

# Usuario - Recurso
usuario_recurso = Table(
    'usuario_recurso',
    Base.metadata,
    Column('id_usuario', Integer, ForeignKey('usuario.id_usuario'), primary_key=True),
    Column('id_recurso', Integer, ForeignKey('recurso.id_recurso'), primary_key=True),
    
)

# Recurso - Etiqueta
recurso_etiqueta = Table(
    'recurso_etiqueta',
    Base.metadata,
    Column('id_recurso', Integer, ForeignKey('recurso.id_recurso'), primary_key=True),
    Column('id_etiqueta', Integer, ForeignKey('etiqueta.id_etiqueta'), primary_key=True)
)

# Tema - Subtema
tema_subtema = Table(
    'tema_subtema',
    Base.metadata,
    Column('id_tema', Integer, ForeignKey('tema.id_tema'), primary_key=True),
    Column('id_subtema', Integer, ForeignKey('subtema.id_subtema'), primary_key=True)
)


# Membresias - beneficios
membresias_beneficios = Table(
    'membresias_beneficios',
    Base.metadata,
    Column('id_membresia', Integer, ForeignKey('membresia.id_membresia'), primary_key=True),
    Column('id_beneficio', Integer, ForeignKey('beneficio.id_beneficio'), primary_key=True)
)