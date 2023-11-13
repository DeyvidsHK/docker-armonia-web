from fastapi import APIRouter
from app.schemas.client_schemas import get_client_db, GetClient, CreateClient, create_client_db, ResponseClient, LoginCredentials, login_db

client_route = APIRouter()

@client_route.get('/GetClient', response_model=GetClient, summary="Obtiene la lista de clientes")
async def get_client():
    return get_client_db()

@client_route.post('/CreateClient', response_model=ResponseClient, summary="Crear clientes")
async def create_client(clientData: CreateClient):
    return create_client_db(clientData)

@client_route.post('/Login', response_model=ResponseClient,summary="Inicio de sesión")
async def login(userData: LoginCredentials):
    return login_db(userData)