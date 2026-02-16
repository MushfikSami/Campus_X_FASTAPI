from fastapi import FastAPI 
from prometheus_fastapi_instrumentator import Instrumentator 

app=FastAPI() 

Instrumentator.instrument(app).expose(app)

@app.get('/home')
def root():
    return {'message':'FastAPI Prometheus with docker'}