import time 
from fastapi import FastAPI 

app=FastAPI()

def computation(i:int):
    res=0
    for n in range(i):
        res+=(i*2)
    time.sleep(1)
    return res    

@profile 
def process_data(x:int):
    return computation(x)



@app.get('/profile')
def get_profile(x:int):
    return {'result':process_data(x)}

