from fastapi import APIRouter
from app.schemas.venta_schemas import ParametrosCreateSell, CreateSellResponse, create_sell_new

venta_router = APIRouter()

@venta_router.post("/CreateSell", summary="Crear venta", response_model=CreateSellResponse)
def create_sell(parametroSell: ParametrosCreateSell):
    return create_sell_new(parametroSell)