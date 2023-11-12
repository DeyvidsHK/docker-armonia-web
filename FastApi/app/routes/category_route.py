from fastapi import APIRouter
from typing import List
from app.schemas.categoria_schemas import get_category_db, GetCategory, create_category_db, CreateCategory, ResponseCreateCategory

categorias_route = APIRouter()

@categorias_route.get('/GetCategory', response_model=GetCategory, summary="Obtiene la lista de categorías")
async def get_category():
    return get_category_db()

@categorias_route.post('/CreateCategory', response_model=ResponseCreateCategory, summary="Crea categorias")
async def create_category(categoryData: CreateCategory):
    return create_category_db(categoryData)