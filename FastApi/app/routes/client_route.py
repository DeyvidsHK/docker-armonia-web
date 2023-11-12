from fastapi import APIRouter
from app.schemas.client_schemas import get_client_db, GetClient

client_route = APIRouter()

@client_route.get('/GetClient', response_model=GetClient, summary="Obtiene la lista de clientes")
async def get_client():
    return get_client_db()