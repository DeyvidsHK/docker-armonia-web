from app.config.connection import create_db_connection
from typing import Optional, List
from app.models.client import client
from sqlalchemy import select
from pydantic import BaseModel

class ListClient(BaseModel):
    id_cliente: int
    nombre: Optional[str]
    correo: str
    usuario: str
    contrasena: str

class GetClient(BaseModel):
    hasClient: bool
    totalItems: int
    message: str
    clientList: Optional[List[ListClient]]

def get_client_db():
    connection_result = create_db_connection()

    if connection_result.success:
        conn = connection_result.connection

        query = select(client)
        result = conn.execute(query).fetchall()

        client_list = [{
            'id_cliente': item.id_cliente,
            'nombre': item.nombre,
            'correo': item.correo,
            'usuario': item.usuario,
            'contrasena': item.contrasena
        } for item in result]

        if client_list:
            message = "Consulta exitosa. Clientes extraidos."
        else:
            message = "No hay clientes."

        return {
            'hasClient': bool(client_list),
            'message': message,
            'totalItems': len(client_list),
            'clientList': client_list
        }

    else:
        return {
            "hasClient": False,
            "message": f"Error en la conexión a la base de datos: {str(connection_result.error_message)}",
            "totalItems": 0,
            "clientList": []
        }