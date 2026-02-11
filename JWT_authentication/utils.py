from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_user_db={
    'Mushfik_Sami':{
        'username':"Mushfik Sami Siam",
        'hashed_password':pwd_context.hash('admin123')
    }
}


def get_user(usename:str):
    user=fake_user_db.get(usename)
    return user 


def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)