from fastapi import APIRouter, UploadFile, BackgroundTasks
from app.schemas.product_schemas import get_product_db, GetProduct, CreateProduct, create_product_db, ResponseCreateProduct

product_route = APIRouter()

@product_route.get('/GetProduct', response_model=GetProduct, summary="Obtiene la lista de productos")
async def get_product():
    return get_product_db()

@product_route.post('/CreateProduct', response_model=ResponseCreateProduct, summary="Crear productos")
async def create_product(productData: CreateProduct, background_tasks: BackgroundTasks):
    # No es necesario leer el contenido de la imagen, ya que ya está en bytes
    image_content = productData.imagen
    
    # Pasa image_content a la función create_product_db
    return create_product_db(productData, image_content)
