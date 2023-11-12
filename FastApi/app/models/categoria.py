# models/categorias.py
from sqlalchemy import Table, Column, Integer, String
from app.config.connection import create_db_connection  

connection_result = create_db_connection()

if connection_result.success:
    metadata = connection_result.metadata
else:
    raise Exception(f"No se pudo establecer la conexión a la base de datos: {connection_result.error_message}")

# Define la tabla usando la Metadata obtenida
categoria = Table('Categorias', metadata,
                    Column('id_categoria', Integer, primary_key=True),
                    Column('nombre', String)
                   )