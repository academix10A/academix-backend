# import httpx
# from app.core.config import settings

# PAYPAL_CLIENT_ID = settings.PAYPAL_CLIENT_ID
# PAYPAL_CLIENT_SECRET = settings.PAYPAL_CLIENT_SECRET
# PAYPAL_API = settings.PAYPAL_API

# # URLs de retorno — PayPal redirige aquí tras aprobar o cancelar.
# # El WebView intercepta estas URLs por la palabra "success" / "cancel".
# RETURN_URL = "https://example.com/paypal/success"
# CANCEL_URL = "https://example.com/paypal/cancel"


# async def get_access_token():
#     async with httpx.AsyncClient() as client:
#         response = await client.post(
#             f"{PAYPAL_API}/v1/oauth2/token",
#             auth=(PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET),
#             data={"grant_type": "client_credentials"}
#         )
#         response.raise_for_status()
#     return response.json()["access_token"]


# async def create_paypal_order(amount: str):
#     token = await get_access_token()

#     async with httpx.AsyncClient() as client:
#         response = await client.post(
#             f"{PAYPAL_API}/v2/checkout/orders",
#             headers={
#                 "Content-Type": "application/json",
#                 "Authorization": f"Bearer {token}"
#             },
#             json={
#                 "intent": "CAPTURE",
#                 "purchase_units": [
#                     {
#                         "amount": {
#                             "currency_code": "MXN",
#                             "value": amount
#                         }
#                     }
#                 ],
#                 # Necesario para el redirect flow (WebView)
#                 "payment_source": {
#                     "paypal": {
#                         "experience_context": {
#                             "return_url": RETURN_URL,
#                             "cancel_url": CANCEL_URL,
#                             # Fuerza la redirección en lugar del popup JS
#                             "user_action": "PAY_NOW",
#                             "landing_page": "LOGIN"
#                         }
#                     }
#                 }
#             }
#         )
#         response.raise_for_status()

#     data = response.json()

#     # Extraer la approval_url del array de links que devuelve PayPal
#     approval_url = next(
#         (link["href"] for link in data.get("links", []) if link["rel"] == "payer-action"),
#         None
#     )

#     # Fallback: algunos flows usan "approve" en lugar de "payer-action"
#     if not approval_url:
#         approval_url = next(
#             (link["href"] for link in data.get("links", []) if link["rel"] == "approve"),
#             None
#         )

#     return {
#         "order_id": data["id"],
#         "approval_url": approval_url,
#     }


# async def capture_paypal_order(order_id: str):
#     token = await get_access_token()

#     async with httpx.AsyncClient() as client:
#         response = await client.post(
#             f"{PAYPAL_API}/v2/checkout/orders/{order_id}/capture",
#             headers={
#                 "Content-Type": "application/json",
#                 "Authorization": f"Bearer {token}"
#             }
#         )
#         response.raise_for_status()

#     data = response.json()
#     status = data["status"]

#     if status != "COMPLETED":
#         return {
#             "success": False,
#             "status": status
#         }

#     capture = data["purchase_units"][0]["payments"]["captures"][0]

#     return {
#         "success": True,
#         "order_id": data["id"],
#         "capture_id": capture["id"],
#         "amount": capture["amount"]["value"],
#         "currency": capture["amount"]["currency_code"],
#         "payer_email": data["payer"]["email_address"]
#     }

import httpx
from app.core.config import settings

PAYPAL_CLIENT_ID = settings.PAYPAL_CLIENT_ID
PAYPAL_CLIENT_SECRET = settings.PAYPAL_CLIENT_SECRET
PAYPAL_API = settings.PAYPAL_API

# Custom scheme — el WebView intercepta esto sin intentar cargar ninguna página real.
# No requiere SSL, no requiere un servidor real, funciona en sandbox y producción.
RETURN_URL = "https://academix.app/paypal/success"
CANCEL_URL = "https://academix.app/paypal/cancel"


async def get_access_token():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYPAL_API}/v1/oauth2/token",
            auth=(PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET),
            data={"grant_type": "client_credentials"}
        )
        response.raise_for_status()
    return response.json()["access_token"]


async def create_paypal_order(amount: str):
    token = await get_access_token()

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYPAL_API}/v2/checkout/orders",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            },
            json={
                "intent": "CAPTURE",
                "purchase_units": [
                    {
                        "amount": {
                            "currency_code": "MXN",
                            "value": amount
                        }
                    }
                ],
                "payment_source": {
                    "paypal": {
                        "experience_context": {
                            "return_url": RETURN_URL,
                            "cancel_url": CANCEL_URL,
                            "user_action": "PAY_NOW",
                            "landing_page": "LOGIN"
                        }
                    }
                }
            }
        )
        response.raise_for_status()

    data = response.json()

    approval_url = next(
        (link["href"] for link in data.get("links", []) if link["rel"] == "payer-action"),
        None
    )

    if not approval_url:
        approval_url = next(
            (link["href"] for link in data.get("links", []) if link["rel"] == "approve"),
            None
        )

    return {
        "order_id": data["id"],
        "approval_url": approval_url,
    }


async def capture_paypal_order(order_id: str):
    token = await get_access_token()

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYPAL_API}/v2/checkout/orders/{order_id}/capture",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )
        response.raise_for_status()

    data = response.json()
    status = data["status"]

    if status != "COMPLETED":
        return {"success": False, "status": status}

    capture = data["purchase_units"][0]["payments"]["captures"][0]

    return {
        "success": True,
        "order_id": data["id"],
        "capture_id": capture["id"],
        "amount": capture["amount"]["value"],
        "currency": capture["amount"]["currency_code"],
        "payer_email": data["payer"]["email_address"]
    }