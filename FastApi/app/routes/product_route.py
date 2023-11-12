from fastapi import APIRouter
from app.schemas.product_schemas import get_product_db, GetProduct

product_route = APIRouter()

@product_route.get('/GetProduct', response_model=GetProduct, summary="Obtiene la lista de productos")
async def get_product():
    return get_product_db()