from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.paypal_service import capture_paypal_order, create_paypal_order
from app.models.membresia import Membresia
from app.crud.crud_usuario_membresia import crear_usuario_membresia
from app.api.deps import get_current_user
from app.models.usuario import Usuario
from app.schemas.paypal import CreateOrderRequest
from datetime import datetime, timedelta
from app.models.usuario_membresia import UsuarioMembresia

router = APIRouter(prefix="/paypal", tags=["Paypal"])


@router.post("/create-order")
async def create_order(
    data: CreateOrderRequest,
    db: Session = Depends(get_db)
):
    membresia = db.query(Membresia).filter(
        Membresia.id_membresia == data.id_membresia
    ).first()

    if not membresia:
        return {"error": "Membresía no encontrada"}

    # create_paypal_order ahora devuelve order_id + approval_url
    order = await create_paypal_order(str(membresia.costo))

    return {
        "orderID": order["order_id"],
        "approvalUrl": order["approval_url"],   # <-- esto es lo que necesita el WebView
    }


@router.post("/capture/{order_id}")
async def capture_payment(
    order_id: str,
    # Flutter manda id_membresia en el body, no en query param
    data: dict,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user)
):
    id_membresia = data.get("id_membresia")

    if not id_membresia:
        return {"success": False, "error": "id_membresia requerido"}

    result = await capture_paypal_order(order_id)

    if not result["success"]:
        return result

    membresia = db.query(Membresia).filter(
        Membresia.id_membresia == id_membresia
    ).first()

    if not membresia:
        return {"success": False, "error": "Membresía no encontrada"}

    # Desactivar membresías activas anteriores
    db.query(UsuarioMembresia).filter(
        UsuarioMembresia.id_usuario == current_user.id_usuario,
        UsuarioMembresia.activa == True
    ).update({"activa": False})

    crear_usuario_membresia(
        db,
        id_usuario=current_user.id_usuario,
        id_membresia=membresia.id_membresia
    )

    user = db.query(Usuario).filter(
        Usuario.id_usuario == current_user.id_usuario
    ).first()

    user.id_rol = 3

    db.commit()
    db.refresh(user)

    return {
        "success": True,
        "message": "Membresía activada"
    }