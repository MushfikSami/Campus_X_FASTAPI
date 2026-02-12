from fastapi import FastAPI, Header, HTTPException, Depends 
from pydantic_settings import BaseSettings 


class Settings(BaseSettings):
    api_key:str 

    class config:
        env_file='.env' 

app=FastAPI()
setting=Settings()


def get_api_key(api_key:str=Header(...)):
    if setting.api_key!=api_key:
        raise HTTPException(status_code=403,detail='Unauthorized')
    
    return api_key 


@app.get('/data')
def get_data(api_key:str=Depends(get_api_key)):
    return {'Output':'Access Granted'}