from fastapi import APIRouter 
from pydantic import BaseModel 
from app.core.security import create_token 


router=APIRouter()

class AuthInput(BaseModel):
    usename:str 
    password:str 


@router.post('/login')
def login(auth:AuthInput):
    if (auth.usename=='admin') and (auth.password=='admin'):
        token=create_token({'sub':auth.usename})
        return {'access_token':token}
    return {'error':'invalid credentials'}

