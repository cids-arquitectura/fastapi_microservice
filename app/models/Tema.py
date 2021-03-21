import logging

from pydantic import ValidationError

from app.models.MasterModel import MasterModel

logger = logging.getLogger(__name__)


class Tema(MasterModel):
    id: int
    nombre: str
    descripcion: str
    duracion: int

    def save(self):
        salida = self.call_sp("PR_EDIT_TEMA",
                              (self.id, self.nombre, self.descripcion, self.duracion),
                              with_return_cursor=False)
        logger.info(salida)

    # con que SP lo cargamos y el resultado en tupla del mismo
    @staticmethod
    def load(from_where, data):
        try:
            if from_where in ['PR_OBTENER_TEMAS', 'PR_OBTENER_TEMA_ID']:
                return Tema(
                    id=data[0],
                    nombre=data[1],
                    descripcion=data[2],
                    duracion=data[3],
                )
            else:
                raise Exception('Error loading object from ' + from_where)
        except ValidationError:
            raise Exception('Validation error ' + from_where + str(data))

    # funciones manager --------------------------
    @staticmethod
    def get_all():
        temas = []
        ret_cursor = Tema.call_sp("PR_OBTENER_TEMAS", None)
        for line in ret_cursor:
            temas.append(Tema.load("PR_OBTENER_TEMAS", line))
        return temas

    @staticmethod
    def get_by_id(request_id):
        tema = None
        ret_cursor = Tema.call_sp("PR_OBTENER_TEMA_ID", (request_id, ))
        for line in ret_cursor:
            tema = Tema.load("PR_OBTENER_TEMA_ID", line)
        return tema
