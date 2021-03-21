from typing import List
from fastapi import APIRouter, HTTPException
from app.models.Persona import Persona
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/personas",
                   tags=["personas"], )


@router.get("/", response_model=List[Persona])
def personas_get_all():
    # personas = Persona.get_all()
    personas = []
    logger.info('personas %s', personas)

    return personas


@router.get('/{persona_id}', response_model=Persona)
def get_detail(persona_id: int):
    persona = Persona.get_by_id(persona_id)
    if persona is None:
        raise HTTPException(status_code=404, detail=f"Persona con id:{persona_id} not found")

    return persona


@router.put('/{persona_id}', response_model=Persona)
def update_detail(persona_id: int, persona: Persona):
    persona_original = Persona.get_by_id(persona_id)
    print(persona)
    return persona
