from fastapi import FastAPI
from app.routes.categoria_route import categorias_route

app = FastAPI()

app.include_router(categorias_route, prefix="/api/Category", tags=['Category'])