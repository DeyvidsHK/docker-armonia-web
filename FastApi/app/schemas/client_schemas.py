from app.config.connection import create_db_connection
from typing import Optional, List
from app.models.client import client
from sqlalchemy import select, insert, select, or_
from pydantic import BaseModel
from app.config.encryption import hash_password

class CreateClient(BaseModel):
    nombre: str
    correo: str
    usuario: str
    contrasena: str

class ResponseCreateClient(BaseModel):
    success: bool
    message: str

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

def validate_existing_user(CreateClient):
    connection_result = create_db_connection()

    if connection_result.success:
        conn = connection_result.connection

        # Verificar si el usuario o el correo ya existen
        query = select(client).where(or_(
            client.c.usuario == CreateClient.usuario.upper(),
            client.c.correo == CreateClient.correo
        ))

        existing_user_result = conn.execute(query)
        existing_user = existing_user_result.fetchone()

        if existing_user:
            if existing_user.usuario == CreateClient.usuario.upper():
                return {
                    "success": True,
                    "message": "El usuario ya existe. Por favor, elija otro nombre de usuario."
                }
            else:
                return {
                    "success": True,
                    "message": "El correo electrónico ya está registrado. Por favor, elija otro correo."
                }
        else:
            return {
                "success": False,
                "message": "El correo electrónico ya está registrado. Por favor, elija otro correo."
            }

def create_client_db(CreateClient):
    connection_result = create_db_connection()

    if connection_result.success:
        conn = connection_result.connection

        existing_user = validate_existing_user(CreateClient)

        if existing_user["success"]:
            return existing_user
        else:
            # Verificar campos no vacíos
            if not CreateClient.nombre or not CreateClient.correo or not CreateClient.usuario or not CreateClient.contrasena:
                return {
                    "success": False,
                    "message": "Los campos no tienen que estar vacios."
                }
            # Hacemos nuestro objeto para crear un nuevo cliente.
            new_client  = {
                'nombre': CreateClient.nombre,
                'correo': CreateClient.correo,
                'usuario': (CreateClient.usuario).upper(),
                'contrasena': hash_password(CreateClient.contrasena)
            }

            # Insertar el nuevo cliente en la base de datos
            query = insert(client).values(new_client)
            result = conn.execute(query)

            # Verificar si la inserción fue exitosa
            if result.rowcount > 0:
                return {
                    "success": True,
                    "message": "Cliente creado exitosamente."
                }
            else:
                return {
                    "success": False,
                    "message": "Error al crear el cliente. Por favor, inténtelo de nuevo."
                }
    else:
        return {
                "success": False,
                "message": "Error en la connexion a la base de datos."
            }


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