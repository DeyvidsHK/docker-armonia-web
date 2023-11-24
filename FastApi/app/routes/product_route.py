from fastapi import APIRouter
from app.schemas.product_schemas import get_product_db, GetProduct, CreateProduct, create_product_db, ResponseCreateProduct

product_route = APIRouter()

@product_route.get('/GetProduct', response_model=GetProduct, summary="Obtiene la lista de productos")
async def get_product():
    return get_product_db()

@product_route.post('/CreateProduct', response_model=ResponseCreateProduct, summary="Crear productos")
async def create_product(productData: CreateProduct):
    return create_product_db(productData)
