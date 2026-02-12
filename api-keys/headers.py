from fastapi import FastAPI, Header, HTTPException ,Depends

app=FastAPI()
API_KEY='mysecretkey'

def get_api_key(api_key:str=Header(...)):
    if api_key!=API_KEY:
        raise HTTPException(status_code=403,detail='Unauthorized')
    return api_key 

@app.get('/get_data')
def get_data(api_key:str=Depends(get_api_key)):
    return {'Output':'Access Granted'}