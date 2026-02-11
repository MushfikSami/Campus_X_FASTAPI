from fastapi import FastAPI,Depends 

app=FastAPI()

def get_db():
    db={'connection':'databse_mock'}
    try:
        yield db 
    finally:
        db.close()


@app.get('/home')
def home(db=Depends(get_db)):
    return {'db status':db['connection']}            