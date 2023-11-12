from app.config.connection import create_db_connection
from typing import Optional, List
from app.models.categoria import categoria
from sqlalchemy import select
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError

class ListCategory(BaseModel):
    id_categoria: int
    nombre: Optional[str]

class GetCategory(BaseModel):
    item: bool
    totalItems: int
    message: str
    ListCategory: Optional[List[ListCategory]]

def get_category_db():
    try:
        connection_result = create_db_connection()
        conn = connection_result.connection

        query = select(categoria)
        result = conn.execute(query)
        rows = result.fetchall()

        category_list = [
            {'id_categoria': item.id_categoria, 'nombre': item.nombre}
            for item in rows
        ]

        if category_list:
            message = "Consulta exitosa. Categorias extraidas."
        else:
            message = "No hay categorías"

        return {
            "item": bool(category_list),
            "message": message,
            "totalItems": len(category_list),
            "ListCategory": category_list
        }
    except SQLAlchemyError as e:
        return {
            "item": False,
            "message": f"Error en la conexión a la base de datos: {str(connection_result.error_message)}",
            "totalItems": 0,
            "ListCategory": []
        }
