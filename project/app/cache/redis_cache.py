import os 
import redis 
from dotenv import load_dotenv 

load_dotenv()

REDIS_URl=os.getenv('REDIS_URL')

redis_client=redis.StrictRedis.from_url(REDIS_URl,decode_response=True)

def get_cached_prediction(key:str):
    value=redis_client.get(key)
    return eval(value) if value else None 

def set_cached_prediction(key:str,value:dict):
    redis_client.set(key,str(value))