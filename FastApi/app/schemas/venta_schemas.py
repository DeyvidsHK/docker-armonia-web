from app.config.connection import create_db_connection
from typing import Optional, List
from app.models.venta import venta
from sqlalchemy import select, insert, select, or_
from app.models.venta import venta
from app.models.detalle_venta import detalle_venta
from pydantic import BaseModel
from datetime import datetime

class ventaParametro(BaseModel):
    id_cliente: Optional[int]
    monto_total: Optional[float]

class detalleVentaParametro(BaseModel):
    id_producto: Optional[int]
    cantidad: Optional[int]
    precio_total: Optional[float]

class ParametrosCreateSell(BaseModel):
    venta: Optional[ventaParametro]
    detalleVenta: Optional[List[detalleVentaParametro]]

class CreateSellResponse(BaseModel):
    success: bool
    message: str

def create_sell_new(create_venta_detalle: ParametrosCreateSell):
    connection_result = create_db_connection()

    if connection_result.success:
        conn = connection_result.connection

        venta_data = {
            "id_cliente": create_venta_detalle.venta.id_cliente,
            "monto_total": create_venta_detalle.venta.monto_total,
            "fecha_venta": datetime.today()
        }

        query_venta = insert(venta).values(venta_data)
        result_venta = conn.execute(query_venta)

        if result_venta.rowcount == 0:
            return {
                "success": False,
                "message": "Error al crear la venta. Por favor, inténtelo de nuevo."
            }

        venta_id = result_venta.lastrowid

        # Crear los detalles de venta
        detalles_venta_data = [
            {
                "id_venta": venta_id,
                "id_producto": detalle.id_producto,
                "cantidad": detalle.cantidad,
                "precio_total": detalle.precio_total
            }
            for detalle in create_venta_detalle.detalleVenta
        ]


        query_detalle_venta = insert(detalle_venta).values(detalles_venta_data)
        result_detalle_venta = conn.execute(query_detalle_venta)

        if result_detalle_venta.rowcount > 0:
            return {
                "success": True,
                "message": "Venta y detalle de venta creados exitosamente."
            }
        else:
            return {
                "success": False,
                "message": "Error al crear el detalle de venta. Por favor, inténtelo de nuevo."
            }

    else:
        return {
            "success": False,
            "message": "Error en la conexión a la base de datos"
        }
