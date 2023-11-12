from app.config.connection import create_db_connection
from typing import Optional, List
from app.models.categoria import categoria
from sqlalchemy import select
from pydantic import BaseModel

class ListCategory(BaseModel):
    id_categoria: int
    nombre: Optional[str]

class GetCategory(BaseModel):
    hasCategory: bool
    totalItems: int
    message: str
    categoryList: Optional[List[ListCategory]]

def get_category_db():

    connection_result = create_db_connection()

    if connection_result.success:
        conn = connection_result.connection

        query = select(categoria)
        result = conn.execute(query).fetchall()

        category_list = [
            {'id_categoria': item.id_categoria, 'nombre': item.nombre}
            for item in result
        ]

        if category_list:
            message = "Consulta exitosa. Categorias extraidas."
        else:
            message = "No hay categorías"

        return {
            "hasCategory": bool(category_list),
            "message": message,
            "totalItems": len(category_list),
            "categoryList": category_list
        }
    else:
        return {
        "hasCategory": False,
        "message": f"Error en la conexión a la base de datos: {str(connection_result.error_message)}",
        "totalItems": 0,
        "categoryList": []
    }