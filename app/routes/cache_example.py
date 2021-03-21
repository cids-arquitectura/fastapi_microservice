from datetime import timedelta
from app.sessions import redis_instance
from fastapi import APIRouter

router = APIRouter(prefix="/cache_example",
                   tags=["cache_example"], )


@router.get("/get_base")
def get_base():
    valor = redis_instance.get('prueba-key')

    return valor


@router.post("/set_base")
def set_base(new_val: str):
    # cuando el parametro no es un modelo, se toma a traves de la URL
    guardado = redis_instance.set('prueba-key', new_val, delta=timedelta(seconds=5))

    return {
        "guardado": guardado,
        "new-value": new_val
    }
