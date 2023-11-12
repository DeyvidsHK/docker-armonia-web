from fastapi import FastAPI
from app.routes.category_route import categorias_route
from app.routes.product_route import product_route

app = FastAPI()

app.include_router(categorias_route, prefix='/api/Category', tags=['Category'])
app.include_router(product_route, prefix='/api/Product', tags=['Product'])