from typing import Dict
from typing import Any
from fastapi import FastAPI

app = FastAPI()

JSON_RESPONSE = Dict[str, Any]


@app.get("/")
def read_root() -> JSON_RESPONSE:
    return {"Hello": "World"}
