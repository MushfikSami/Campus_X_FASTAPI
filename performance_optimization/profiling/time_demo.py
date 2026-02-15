import time
from fastapi import FastAPI,Request 
import logging 

logging.basicConfig(
    level=logging.INFO
)

logger=logging.getLogger('profiler')

app=FastAPI()

@app.middlewire('http')
async def get_time(req:Request,call_next):
    start_time=time.time()
    response=await call_next(req)
    time_taken=time.time() - start_time 
    logger.info(f'{req} took {time_taken} sec')
    return response


@app.get('/')
def home():
    return {'message':'profiling demo'}

@app.get('/slow')
async def slow_endpoint():
    time.sleep(2)
    return {'message':'This is a slow endpoint'}

@app.get('/fast')
async def fast_endpoint():
    return {'message':'This is a fast endpoint'} 