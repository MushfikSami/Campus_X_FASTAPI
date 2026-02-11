from fastapi import FastAPI 
from starlett.middleware.httpsredict import HTTPSRedirectMiddleware

app=FastAPI()

app.add_middleware(HTTPSRedirectMiddleware)