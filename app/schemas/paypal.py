from pydantic import BaseModel

class CreateOrderRequest(BaseModel):
    id_membresia: int