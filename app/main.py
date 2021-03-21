from fastapi import FastAPI, Request
from functools import lru_cache
from app import config
from app.db import Database
from app.sessions import database_instance, redis_instance
from app.routes import temas, personas, alumnos, cache_example
import logging
# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)


@lru_cache()
def get_settings():
    return config.Settings()


def create_app():
    app = FastAPI()
    settings = get_settings()
    db = Database()

    @app.middleware("http")
    async def db_session_middleware(request: Request, call_next):
        request.state.pool = db.pool
        response = await call_next(request)
        return response

    @app.on_event("startup")
    def startup():
        database_instance.create_pool(settings)
        redis_instance.connect(settings)

    @app.on_event("shutdown")
    async def shutdown():
        database_instance.close_pool()
        redis_instance.connect(settings)

    app.include_router(alumnos.router)
    app.include_router(temas.router)
    app.include_router(personas.router)
    app.include_router(cache_example.router)
    return app


app = create_app()
