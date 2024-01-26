import time
from datetime import date
from typing import Any, Dict

import {{cookiecutter.repo_name}}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from {{cookiecutter.repo_name}}.database import SessionLocal
from {{cookiecutter.repo_name}}.services.app import init_app

app = init_app()


START_TIME = time.time()

JSON_RESPONSE = Dict[str, Any]


@app.get("/health_check/", tags=["operations"])
async def health_check():
    return {
        "message": "OK",
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "timestamp": date.fromtimestamp(time.time()),
        "version": {{cookiecutter.repo_name}}.__version__,
    }


@app.get("/")
async def read_root() -> JSON_RESPONSE:
    return {"Hello": "World"}
