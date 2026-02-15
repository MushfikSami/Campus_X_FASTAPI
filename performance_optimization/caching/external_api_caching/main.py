import redis 
import json 
import hashlib
import httpx 
from fastapi import FastAPI 
from pydantic import BaseModel 

app=FastAPI()
redis_client=redis.Redis(host='localhost',port=6379,db=0)

class PostRequest(BaseModel):
    post_id:int 

def make_cache_key(post_id:int):
    raw=f'post_id{post_id}'
    return hashlib.sha256(raw.encode()).hexdigest()


@app.post('/get-post')
async def get_post(post:PostRequest):
    key=make_cache_key(post.post_id)
    cache_data=redis_client.get(key)
    if cache_data:
        return json.loads(cache_data)
    
    async with httpx.AsyncClient() as client:
        response=await client.get(f'https://jsonplaceholder.typicode.com/posts/{post.post_id}')

    result=response.json()
    redis_client.setx(key,600,json.dumps(result))
    return result    