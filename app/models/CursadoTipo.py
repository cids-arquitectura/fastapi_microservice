import logging
from app.models.MasterModel import MasterModel

logger = logging.getLogger(__name__)


class CursadoTipo(MasterModel):
    id: int
    nombre: str

    # con que SP lo cargamos y el resultado en tupla del mismo
    @staticmethod
    def load(from_where, data):
        if from_where in ['PR_OBTENER_CURSADO_TIPO_ID']:
            return CursadoTipo(
                id=data[0],
                nombre=data[1]
            )
        else:
            raise Exception('Error loading object from ' + from_where)

    @staticmethod
    def get_by_id(request_id):
        cursado_tipo = None
        ret_cursor = CursadoTipo.call_sp("PR_OBTENER_CURSADO_TIPO_ID", (request_id, ))
        for line in ret_cursor:
            cursado_tipo = CursadoTipo.load("PR_OBTENER_CURSADO_TIPO_ID", line)
        return cursado_tipo