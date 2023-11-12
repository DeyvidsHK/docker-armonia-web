from fastapi import APIRouter
from schemas.client_schemas import get_client_db

client_route = APIRouter()

@client_route.get('/GetClient')
async def get_client():
    return get_client_db()