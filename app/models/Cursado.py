import logging

from app.models.CursadoTipo import CursadoTipo
from app.models.MasterModel import MasterModel
from app.models.Tema import Tema

logger = logging.getLogger(__name__)


class Cursado(MasterModel):
    tema: Tema
    estado: CursadoTipo

    # con que SP lo cargamos y el resultado en tupla del mismo
    @staticmethod
    def load(from_where, data):
        if from_where in ['PR_OBTENER_CURSADO_ALUMNO']:
            tema = Tema.get_by_id(data[1])
            logger.info('tema %s', tema)
            estado = CursadoTipo.get_by_id(data[2])
            logger.info('estado %s', estado)
            cursado = Cursado(
                tema=tema,
                estado=estado
            )
            return cursado
        else:
            raise Exception('Error loading object from ' + from_where)

    @staticmethod
    def get_by_alumno(request_id):
        cursados = []
        ret_cursor = Cursado.call_sp("PR_OBTENER_CURSADO_ALUMNO", (request_id, ))
        for line in ret_cursor:
            cursados.append(Cursado.load("PR_OBTENER_CURSADO_ALUMNO", line))
        return cursados
