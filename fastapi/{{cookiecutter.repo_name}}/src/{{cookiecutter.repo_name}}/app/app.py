import logging
from contextlib import asynccontextmanager

import {{cookiecutter.repo_name}}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from {{cookiecutter.repo_name}}.config import get_db_connection_url
from {{cookiecutter.repo_name}}.services import sessionmanager

logger = logging.getLogger(__name__)


def init_app(init_db=True) -> FastAPI:
    lifespan = None
    if init_db:
        db_url = get_db_connection_url()
        if not db_url:
            raise Exception(
                "Database connection 'db_url' is not set unable to establish connection",
            )
        sessionmanager.init(db_url)

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            yield
            if sessionmanager._engine is not None:
                await sessionmanager.close()

    server = FastAPI(
        title="{{cookiecutter.repo_name}} API",
        summary="{{cookiecutter.description}}",
        version={{cookiecutter.repo_name}}.__version__,
    )

    origins = ["http://127.0.0.1:4200"]

    server.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from {{cookiecutter.repo_name}}.controllers.user import \
        router as user_router
    server.include_router(
        user_router,
        prefix="/api",
    )

    return server
