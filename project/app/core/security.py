from datetime import datetime, timezone,timedelta
from jose import jwt,JWTError
from app.core.config import settings 



def create_token(data:dict,expire_time=30):
    to_encode=data.copy()
    total_time=datetime.now()+timedelta(expire_time)
    to_encode.update({'exp':total_time})
    return jwt.encode(
        to_encode,settings.JWT_SECRET_KEY,settings.JWT_ALGORITHM
    )


def verify_token(token:str):
    try:
        payload=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError:
        return None 