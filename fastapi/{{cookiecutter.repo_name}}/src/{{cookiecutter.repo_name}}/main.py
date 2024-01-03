import time
from datetime import date
from typing import Dict
from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from {{cookiecutter.repo_name}}.database import SessionLocal
from dotenv import load_dotenv
import {{cookiecutter.repo_name}}

load_dotenv()

app = FastAPI(
    title="{{cookiecutter.repo_name}} API",
    summary="{{cookiecutter.description}}",
    version={{cookiecutter.repo_name}}.__version__,
)

tags_metadata = [
    {
        "name": "operations",
        "description": "Operations and site reliability engineering",
    },
    {
        "name": "{{cookiecutter.repo_name}}",
        "description": "{{cookiecutter.description}}",
    },
]

origins = ["http://127.0.0.1:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        if db:
            db.close()


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
def read_root() -> JSON_RESPONSE:
    return {"Hello": "World"}
