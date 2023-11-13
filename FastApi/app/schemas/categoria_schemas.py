from app.config.connection import create_db_connection
from typing import Optional, List
from app.models.categoria import categoria
from sqlalchemy import select, insert, select, or_
from pydantic import BaseModel

class CreateCategory(BaseModel):
    nombre: str

class ResponseCreateCategory(BaseModel):
    success: bool
    message: str

class ListCategory(BaseModel):
    id_categoria: int
    nombre: Optional[str]

class GetCategory(BaseModel):
    hasCategory: bool
    totalItems: int
    message: str
    categoryList: Optional[List[ListCategory]]

def validate_existing_category(conn, category_name):
    # Crear un objeto de selección
    query = select(categoria).where(categoria.c.nombre == category_name)

    # Ejecutar la consulta
    result = conn.execute(query)

    # Verificar si se encontró alguna fila
    existing_category = result.fetchone()

    if existing_category:
        return {
            "success": True,
            "message": f"La categoría {category_name} ya existe en la base de datos. Por favor, elija otro nombre de categoría."
        }
    else:
        return {
            "success": False,
            "message": "La categoría no existe en la base de datos. Puede usar este nombre para una nueva categoría."
        }


def create_category_db(CreateCategory):
    connection_result = create_db_connection()

    if connection_result.success:
        if not CreateCategory.nombre:
            return {
                "success": False,
                "message": "Ingrese un nombre a la categoria, no tienen que estar vacios."
            }
        else:
            conn = connection_result.connection

            existing_category = validate_existing_category(conn, CreateCategory.nombre)

            if existing_category["success"]:
                return {
                    "success": False,
                    "message": existing_category["message"]
                }
            else:
                # Insertar el nuevo cliente en la base de datos
                query = insert(categoria).values(nombre=CreateCategory.nombre)
                result = conn.execute(query)

                # Verificar si la inserción fue exitosa
                if result.rowcount > 0:
                    return {
                        "success": True,
                        "message": "Categoria creado exitosamente."
                    }
                else:
                    return {
                        "success": False,
                        "message": "Error al crear la categoria. Por favor, inténtelo de nuevo."
                    }
    else:
        return {
                    "success": False,
                    "message": "Error en la connexion a la base de datos."
                }

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