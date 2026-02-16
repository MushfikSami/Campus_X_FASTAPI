from fastapi import FastAPI 
from prometheus_fastapi_instrumentator import Instrumentator 

app=FastAPI()

Instrumentator.instrument(app).expose(app)

@app.get('/home')
def root():
    return {'message':'Run Fastapi with, grafana, promethus and docker'}


@app.get('/ping')
def ping():
    return {'message':'pong'}