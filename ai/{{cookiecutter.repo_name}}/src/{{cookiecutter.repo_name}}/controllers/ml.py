from datetime import datetime
import keras
import numpy as np
from pydantic_settings import BaseSettings

from fastapi import APIRouter
from pydantic import BaseModel

# NOTE: descriptive model name goes here
router = APIRouter(prefix="/{{cookiecutter.model_name}}", tags=["model", "{{cookiecutter.model_name}}"])


class Settings(BaseSettings):
    ai_model_url: str


settings = Settings()
model = None

if settings.ai_model_url.startswith("file:///"):
    model_path: str = settings.ai_model_url[7:]
    model = keras.models.load_model(model_path)
else:
    raise RuntimeError("AI_MODEL_URL environment variable must be set")


# TODO: Update the model to include the data this model requires as input
# which ideally is a list of parameter names but getting started with a
# tensor is fine for prototyping.
class InferenceRequest(BaseModel):
    input: list[list[float]]


# Regression
#
@router.post("/inference")
async def post_predict_regression(req: InferenceRequest):
    # model_path: str = settings.ai_model_url[7:]
    # model = keras.models.load_model(model_path)
    prediction = model.predict(x = np.array(req.input))
    now: str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    return {
            "prediction": round(float(prediction[0][0]), 2),
            "created_at": now,
        }

# Categorical
#
#@router.post("/inference")
#async def post_predict_category(req: InferenceRequest):
#    prediction = np.argmax(model.predict(x = np.array(req.input)), axis=1)
#    now: str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
#    return {
#            "prediction": prediction[0][0],
#            "created_at": now,
#        }

# Binary
#
#@router.post("/inference")
#async def post_predict_binary(req:InferenceRequest):
#    threshold = 0.49
#    prediction = np.where(model.predict(x = np.array(req.input)) > threshold, 1, 0)
#    now: str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
#    return {
#            "prediction": prediction[0][0],
#            "created_at": now,
#        }
