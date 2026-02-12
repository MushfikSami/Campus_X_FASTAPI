from fastapi import HTTPException
from datetime import datetime, timedelta, timezone 
from authlib.jose import jwt,JoseError


SECRET_KEY='secret_key'
ALGORITHM='HS256'
ACESS_TOKEN_EXPIRE_MINUTES=10 

def create_access_token(data:dict):
    header={'alg':ALGORITHM}
    expire=datetime.now()+timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    payload=data.copy()
    payload.update({"exp": expire})
    return jwt.encode(header,payload,SECRET_KEY).decode('utf-8')


def verify_access_token(token:str):
    try:
        claim=jwt.decode(token,SECRET_KEY)
        claim.validate()
        username=claim.get('sub')
        if username is None:
            raise HTTPException(status_code=401,detail='Invalid token')
        return username
    except JoseError:
        raise HTTPException(status_code=401,detail='Could not validate token')