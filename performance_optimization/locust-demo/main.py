from fastapi import FastAPI 
from pydantic import BaseModel

app=FastAPI()

class InputData(BaseModel):
    feature1:int 
    feature2:int 


@app.get('/')
def home():
    return {'messages':'Locust Demo'}


@app.post('/predict')
def predict(data:InputData):
    result=data.feature1+data.feature2
    return {'result':result}
