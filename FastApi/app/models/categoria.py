# models/categorias.py
from sqlalchemy import Table, Column, Integer, String
from app.config.connection import metadata


# Define la tabla usando la Metadata obtenida
categoria = Table('Categorias', metadata,
                    Column('id_categoria', Integer, primary_key=True),
                    Column('nombre', String)
                   )