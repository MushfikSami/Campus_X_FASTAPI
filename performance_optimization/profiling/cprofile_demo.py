import os 
import time 
import cProfile 
import datetime 
from fastapi import FastAPI,Request 
from fastapi.responses import JSONResponse 

profiles_dir='profiles'
os.makedirs(profiles_dir,exist_ok=True)

app=FastAPI()

@app.middleware('http')
async def create_profile(req:Request,call_next):
    time_stamp=datetime.datetime.now()
    path=req.url.path.strip('/').replace('/','_') or 'root'
    profile_name=os.path.join(profiles_dir,f'{path}_{time_stamp}.prof')

    profiler=cProfile.Profile()
    profiler.enable()
    response=await call_next(req)
    profiler.disable()
    profiler.dump_stats(profile_name)
    return response 

@app.get('/')
def home():
    return {'message':'cProfile demo'} 


@app.get('/compute')
async def compute():
    time.sleep(1)
    result= sum((i*2) for i in range(1000))
    return JSONResponse({'result':result})