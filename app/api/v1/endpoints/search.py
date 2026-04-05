from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.crud.crud_search import get_search

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/")
def search(
    busqueda: str = Query(..., min_length=1),
    tipo: str = Query("all"),
    db: Session = Depends(get_db)
):
    return get_search(db, busqueda, tipo)

