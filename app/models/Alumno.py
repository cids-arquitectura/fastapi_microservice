import logging
from typing import List

from app.models.Cursado import Cursado
from app.models.MasterModel import MasterModel
from app.models.Persona import Persona

logger = logging.getLogger(__name__)


class Alumno(MasterModel):
    id: int
    id_reparticion: int
    persona: Persona
    cursado: List[Cursado]

    # con que SP lo cargamos y el resultado en tupla del mismo
    @staticmethod
    def load(from_where, data):
        if from_where in ['PR_OBTENER_PERSONAS', 'PR_OBTENER_ALUMNO_ID']:
            persona = Persona.get_by_id(data[1])
            logger.info('persona %s', persona)

            cursado = Cursado.get_by_alumno(data[0])
            logger.info('cursado %s', cursado)

            alumno = Alumno(
                id=data[0],
                id_reparticion=data[2],
                persona=persona,
                cursado=cursado
            )
            return alumno
        else:
            raise Exception('Error loading object from ' + from_where)

    @staticmethod
    def get_by_id(request_id):
        alumno = None
        ret_cursor = Alumno.call_sp("PR_OBTENER_ALUMNO_ID", (request_id, ))
        for line in ret_cursor:
            alumno = Alumno.load("PR_OBTENER_ALUMNO_ID", line)
        return alumno
