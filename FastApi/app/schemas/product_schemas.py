from app.config.connection import create_db_connection
from app.config.connection import create_db_connection
from typing import Optional, List
from app.models.product import product
from sqlalchemy import select
from pydantic import BaseModel

class ListProduct(BaseModel):
    id_producto: int
    nombre: Optional[str]
    descripcion: str
    precio: float
    stock: int
    imagen: str
    id_categoria: int

class GetProduct(BaseModel):
    hasProduct: bool
    totalItems: int
    message: str
    productList: Optional[List[ListProduct]]

def get_product_db():

    connection_result = create_db_connection()

    if connection_result.success:
        conn = connection_result.connection

        query = select(product)
        result = conn.execute(query).fetchall()

        product_list = [
            { 
                'id_producto': item.id_producto,
                'nombre': item.nombre, 
                'descripcion': item.descripcion, 
                'precio': item.precio, 
                'stock': item.stock, 
                'imagen': item.imagen, 
                'id_categoria': item.id_categoria
            } for item in result
        ]

        if product_list:
            message = "Consulta exitosa. Productos extraidos."
        else:
            message = "No hay productos."

        return {
            'hasProduct': bool(product_list),
            'message': message,
            'totalItems': len(product_list),
            'productList': product_list
        }

    else:
        return {
            "hasProduct": False,
            "message": f"Error en la conexión a la base de datos: {str(connection_result.error_message)}",
            "totalItems": 0,
            "productList": []
        }