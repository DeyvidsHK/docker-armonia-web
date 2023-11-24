# models/product.py
from sqlalchemy import Table, Column, Integer, String, Float, LargeBinary
from app.config.connection import metadata

product = Table('Productos', metadata,
                 Column('id_producto', Integer, primary_key=True),
                 Column('nombre', String),
                 Column('descripcion', String),
                 Column('precio', Float),
                 Column('stock', Integer),
                 Column('imagen', LargeBinary),
                 Column('id_categoria', Integer)
                )