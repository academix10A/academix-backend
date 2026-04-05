from pydantic import BaseModel
from datetime import datetime


class OfflineBase(BaseModel):
    id_recurso: int


class OfflineCreate(OfflineBase):
    pass


class OfflineResponse(OfflineBase):
    id: int
    fecha_descarga: datetime
    activo: bool

    class Config:
        from_attributes = True