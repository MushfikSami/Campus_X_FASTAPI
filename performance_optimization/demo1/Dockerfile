FROM python:3.12 

workdir /app 

copy ./app /app 


run pip install fastapi uvicorn prometheus-fastapi-instrumentator 

cmd ['uvicorn','main:app','--host','0.0.0.0','--port','8000']