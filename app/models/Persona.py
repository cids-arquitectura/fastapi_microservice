import logging
from app.models.MasterModel import MasterModel

logger = logging.getLogger(__name__)


class Persona(MasterModel):
    id: int
    nombre: str
    apellido: str
    edad: int
    cuil: str

    # con que SP lo cargamos y el resultado en tupla del mismo
    @staticmethod
    def load(from_where, data):
        if from_where in ['PR_OBTENER_PERSONAS', 'PR_OBTENER_PERSONA_ID']:
            return Persona(
                id=data[0],
                nombre=data[1],
                apellido=data[2],
                edad=data[3],
                cuil=data[4],
            )
        else:
            raise Exception('Error loading object from ' + from_where)

    @staticmethod
    def get_by_id(request_id):
        persona = None
        ret_cursor = Persona.call_sp("PR_OBTENER_PERSONA_ID", (request_id, ))
        for line in ret_cursor:
            persona = Persona.load("PR_OBTENER_PERSONA_ID", line)
        return persona