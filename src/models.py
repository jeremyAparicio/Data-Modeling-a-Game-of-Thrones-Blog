import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    correo = Column(String(250), nullable=False)
    contraseña = Column(String(250), nullable=False)

class Personajes(Base):
    __tablename__ = 'personaje'
    id_personaje = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    titulo = Column(String(250))
    casa= Column(String(250), nullable=False)
    perso_a_casa = Column(Integer, ForeignKey('casa.id_casa'))
    perso_a_conti = Column(Integer, ForeignKey('continente.id_continente'))
    perso_a_fav = Column(Integer, ForeignKey('favorito.id_favoritos'))

class Casas(Base):
    __tablename__ = 'casa'
    id_casa = Column(Integer, primary_key=True)
    nombre = Column(String(250))

class Continentes(Base):
    __tablename__ = 'continente'
    id_continente = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    conti_a_fav = Column(Integer, ForeignKey('favorito.id_favoritos'))

class Favoritos(Base):
    __tablename__ = 'favorito'
    id_favoritos = Column(Integer, primary_key=True)
    user_a_fav = Column(Integer, ForeignKey('usuario.id_usuario'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
