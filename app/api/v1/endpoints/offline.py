from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_active_user
from app.models.usuario import Usuario
from app.models.recurso import Recurso
from app.crud import crud_offline

from app.core.permissions import PermissionChecker, Beneficios

router = APIRouter(prefix="/offline", tags=["Offline"])


@router.post(
    "/{id_recurso}",
    dependencies=[Depends(PermissionChecker(beneficios=[Beneficios.DESCARGA]))]
)
def descargar(
    id_recurso: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    recurso = db.query(Recurso).filter(Recurso.id_recurso == id_recurso).first()

    if not recurso:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

    return crud_offline.descargar_recurso(
        db,
        id_usuario=current_user.id_usuario,
        id_recurso=id_recurso
    )


@router.get(
    "/",
    dependencies=[Depends(PermissionChecker(beneficios=[Beneficios.MODO_OFFLINE]))]
)
def mis_descargas(
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    descargas = crud_offline.obtener_descargas(
        db,
        id_usuario=current_user.id_usuario
    )

    return [
        {
            "id_recurso": o.recurso.id_recurso,
            "titulo": o.recurso.titulo,
            "descripcion": o.recurso.descripcion,
            "url": o.recurso.url_archivo,
            "fecha_descarga": o.fecha_descarga
        }
        for o in descargas
    ]


@router.delete(
    "/{id_recurso}",
    dependencies=[Depends(PermissionChecker(beneficios=[Beneficios.DESCARGA]))]
)
def eliminar(
    id_recurso: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_active_user)
):
    result = crud_offline.eliminar_descarga(
        db,
        id_usuario=current_user.id_usuario,
        id_recurso=id_recurso
    )

    if not result:
        raise HTTPException(status_code=404, detail="No encontrado")

    return {"message": "Eliminado"}



