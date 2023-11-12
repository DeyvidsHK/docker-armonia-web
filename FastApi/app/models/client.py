# models/client.py
from app.config.connection import metadata
from sqlalchemy import Table, Column, Integer, String, Float

client = Table('Clientes', metadata, 
                Column('id_cliente', Integer, primary_key=True),
                Column('nombre', String),
                Column('correo', String),
                Column('usuario', String),
                Column('contrasena', String)
               )