import time
from datetime import date
from typing import Any, Dict

from {{cookiecutter.repo_name}} import __version__ as version
from {{cookiecutter.repo_name}}.app import init_app

app = init_app()


START_TIME = time.time()

JSON_RESPONSE = Dict[str, Any]


@app.get("/health_check/", tags=["operations"])
async def health_check():
    return {
        "message": "OK",
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "timestamp": date.fromtimestamp(time.time()),
        "version": version
    }


@app.get("/")
async def read_root() -> JSON_RESPONSE:
    return {"Hello": "World"}
