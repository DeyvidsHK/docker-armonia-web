from fastapi import APIRouter
from typing import List
from app.schemas.categoria_schemas import get_category_db, GetCategory

categorias_route = APIRouter()

@categorias_route.get('/GetCategory', response_model=GetCategory, summary="Obtiene la lista de categorías")
async def get_category():
    return get_category_db()