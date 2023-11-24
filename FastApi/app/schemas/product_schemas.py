from app.config.connection import create_db_connection
from typing import Optional, List
from app.models.product import product
from sqlalchemy import select, insert, select, or_
from pydantic import BaseModel

class CreateProduct(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    imagen: str
    id_categoria: int

class ResponseCreateProduct(BaseModel):
    success: bool
    message: str

class ListProduct(BaseModel):
    id_producto: int
    nombre: Optional[str]
    descripcion: str
    precio: float
    stock: int
    imagen: bytes
    id_categoria: int

class GetProduct(BaseModel):
    hasProduct: bool
    totalItems: int
    message: str
    productList: Optional[List[ListProduct]]


def validate_existing_product(conn, CreateProduct):
    query = select(product).where(product.c.nombre == CreateProduct.nombre)
    result = conn.execute(query)

    existing_product = result.fetchone()

    if existing_product:
        return {
                "success": True,
                "message": f"El producto '{existing_product.nombre}' ya existe."
                }
    else:
        return {
                "success": False,
                "message": "El producto no existe."
                }

def create_product_db(CreateProduct):

    connection_result = create_db_connection()

    if connection_result.success:
        if not CreateProduct.nombre or not CreateProduct.descripcion or not CreateProduct.precio or not CreateProduct.stock or not CreateProduct.imagen or not CreateProduct.id_categoria:
            return {
                "success": False,
                "message": "Los campos no deben estar vacíos."
            }
        else:
            conn = connection_result.connection

            existing_product = validate_existing_product(conn, CreateProduct)

            if existing_product["success"]:
                return {
                    "success": False,
                    "message": existing_product["message"]
                }
            else:
                # Producto no existe en la base de datos y se tiene que crear.
                new_product = {
                    "nombre": CreateProduct.nombre,
                    "descripcion": CreateProduct.descripcion,
                    "precio": CreateProduct.precio,
                    "stock": CreateProduct.stock,
                    "imagen": CreateProduct.imagen,  # Asegúrate de que la imagen esté codificada en bytes
                    "id_categoria": CreateProduct.id_categoria
                }

                # Insertar el nuevo cliente en la base de datos
                query = insert(product).values(new_product)
                result = conn.execute(query)

                # Verificar si la inserción fue exitosa
                if result.rowcount > 0:
                    return {
                        "success": True,
                        "message": "Producto creado exitosamente."
                    }
                else:
                    return {
                        "success": False,
                        "message": "Error al crear el producto. Por favor, inténtelo de nuevo."
                    }
    else:
        return {
            "success": False,
            "message": "Error en la conexión a la base de datos."
        }


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