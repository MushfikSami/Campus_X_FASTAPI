from fastapi import Request,FastAPI 
from fastapi.responses import JSONResponse 

app=FastAPI()


@app.exception_handler(Exception)
def general_exception_handler(req:Request,exc:Exception):
    return JSONResponse(
        status_code=500,
        content={'error':str(exc)}
    )



@app.get('/exception')
def handle_exeption():
    return 1/0