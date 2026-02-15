import redis 
import json 
import hashlib
import joblib 
from fastapi import FasAPI 
from pydantic import BaseModel 


app=FasAPI()
redis_clinet=redis.Redis(host='localhost',port=6379,db=0)

model=joblib.load('model.joblib')

class Flower(BaseModel):
    SepalLengthCm:float 
    SepalWidthCm:float
    PetalLengthCm:float
    PetalWidthCm:float 

    def to_list(self):
        return [
            self.SepalLengthCm,
            self.SepalWidthCm,
            self.PetalLengthCm,
            self.PetalWidthCm
        ]
    
    def cache_key(self):
        raw=json.dumps(self.model_dump(),sort_keys=True)
        return f'Predict: {hashlib.sha256(raw.encode()).hexdigest()}'
    


@app.post('/predict')
async def predict(data:Flower):
    key=data.cache_key() 

    cached_result=redis_clinet.get(key)
    if cached_result:
        return json.loads(cached_result)

    prediction=model.predict(data.to_list())[0]
    result={"predictions ":int(prediction)}
    redis_clinet.set(key,json.dumps(result),ex=3600)
    return result    