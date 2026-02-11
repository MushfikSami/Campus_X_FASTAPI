import time
from fastapi import FastAPI,Request 
from starlette.middleware.base import BaseHTTPMiddleware

app=FastAPI()

class CustomMiddleware(BaseHTTPMiddleware):
    async def resposive(self,request:Request,call_next):
        start_time=time.time()
        response=await call_next(request)
        duration=start_time-time.time()
        print(f"Request duration: {duration} seconds")
        return response    
    
app.add_middleware(CustomMiddleware)

app.get('/')
async def root():
    for _ in range(1000000):
        pass
    return {'message':'Hello World'}