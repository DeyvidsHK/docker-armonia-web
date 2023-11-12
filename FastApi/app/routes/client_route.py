from fastapi import APIRouter
from app.schemas.client_schemas import get_client_db, GetClient, CreateClient, create_client_db, ResponseCreateClient

client_route = APIRouter()

@client_route.get('/GetClient', response_model=GetClient, summary="Obtiene la lista de clientes")
async def get_client():
    return get_client_db()

@client_route.post('/CreateClient', response_model=ResponseCreateClient, summary="Crear clientes")
async def create_client(clientData: CreateClient):
    return create_client_db(clientData)