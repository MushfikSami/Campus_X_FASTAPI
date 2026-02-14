import logging 
from fastapi import FastAPI 

app=FastAPI()

logging.basicConfig(
    level=logging.INFO
)


@app.get('/debug')
def get_debug():
    logging.info('Debug endpoint hit')
    logging.info('Another endpoint hit')
    return {'message':'check logs'}