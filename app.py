import uvicorn
from fastapi import FastAPI,Path, Query, HTTPException
from pydantic import BaseModel
from typing import Union
from typing_extensions import Annotated
from roboflow import Roboflow
from model import get_car_damage

class Image(BaseModel):
    url: str

app = FastAPI()

@app.get('/')
async def health():
  return {"message": "app is running"}

# @app.post("/predict_damage/")
# async def get_car_damages(image: Image):
#     return get_car_damage(image)

@app.get('/predict_damage/{image_path:path}')
def pred_image(image_path: str):
    return get_car_damage(image_path)


if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, host= '127.0.0.1')