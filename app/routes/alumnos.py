from typing import List
from fastapi import APIRouter, HTTPException
from app.models.Alumno import Alumno
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/alumnos",
                   tags=["alumnos"], )


@router.get("/", response_model=List[Alumno])
def alumnos_get_all():
    # alumnos = Alumno.get_all()
    alumnos = []
    logger.info('alumnos %s', alumnos)

    return alumnos


@router.get('/{alumno_id}', response_model=Alumno)
def get_detail(alumno_id: int):
    alumno = Alumno.get_by_id(alumno_id)
    if alumno is None:
        raise HTTPException(status_code=404, detail=f"Alumno con id:{alumno_id} not found")

    return alumno


@router.put('/{persona_id}', response_model=Alumno)
def update_detail(alumno_id: int, alumno: Alumno):
    alumno_original = Alumno.get_by_id(alumno_id)
    print(alumno)
    return alumno
