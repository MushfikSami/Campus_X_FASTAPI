from python:3.12 

workdir /app 

copy app/main.py 

copy requirements.txt 

run pip install --no-cache-dir -r requirements.txt 

cmd['uvicorn','main:app','--host','0.0.0.0','--port','8000']