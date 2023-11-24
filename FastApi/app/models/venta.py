from sqlalchemy import Table, Column, Integer, String, Float, DateTime
from app.config.connection import metadata

venta = Table('Ventas', metadata,
                 Column('id_venta', Integer, primary_key=True),
                 Column('monto_total', Float),
                 Column('fecha_venta', DateTime),
                 Column('id_cliente', Integer)
                )