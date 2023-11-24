from sqlalchemy import Table, Column, Integer, String, Float, DateTime
from app.config.connection import metadata

detalle_venta = Table('DetallesVenta', metadata,
                 Column('id_detalle', Integer, primary_key=True),
                 Column('id_venta', Integer),
                 Column('id_producto', Integer),
                 Column('precio_total', Float),
                 Column('cantidad', Integer)
                )