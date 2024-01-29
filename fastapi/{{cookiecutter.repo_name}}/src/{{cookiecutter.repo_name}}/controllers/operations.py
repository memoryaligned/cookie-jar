import time
from datetime import date
from typing import Any, Dict

import {{cookiecutter.repo_name}}
from fastapi import APIRouter

START_TIME = time.time()
JSON_RESPONSE = Dict[str, Any]

router = APIRouter(prefix="/ops", tags=["operations"])


@router.get("/health_check/", tags=["operations"])
async def health_check():
    return {
        "message": "OK",
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "timestamp": date.fromtimestamp(time.time()),
        "version": {{cookiecutter.repo_name}}.__version__,
    }


@router.get("/")
async def read_root() -> JSON_RESPONSE:
    return {
        "Hello": "World",
    }
