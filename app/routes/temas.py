from typing import List
from fastapi import APIRouter, HTTPException
from app.models.Tema import Tema
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/temas",
                   tags=["temas"], )


@router.get("/", response_model=List[Tema])
def temas_get_all():
    temas = Tema.get_all()
    logger.info('temas %s', temas)

    return temas


@router.get('/{tema_id}', response_model=Tema)
def get_detail(tema_id: int):
    tema = Tema.get_by_id(tema_id)
    if tema is None:
        raise HTTPException(status_code=404, detail=f"Tema con id:{tema_id} not found")
    return tema


@router.put('/{tema_id}', response_model=Tema)
def update_detail(tema_id: int, tema: Tema):
    tema_original = Tema.get_by_id(tema_id)
    print(tema)
    return tema
