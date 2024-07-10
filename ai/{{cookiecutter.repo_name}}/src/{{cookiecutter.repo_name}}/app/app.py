import logging

import {{cookiecutter.repo_name}}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger(__name__)


def init_app() -> FastAPI:
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

    from {{cookiecutter.repo_name}}.controllers import ops_router, ml_router
    server.include_router(
        ml_router,
        prefix="/ai",
    )

    server.include_router(
        ops_router,
        prefix="/api",
    )

    return server
