from fastapi import FastAPI 
from pydantic import BaseModel

class Applicant(BaseModel):
    age:int 
    income:float 
    employment_status:str 

app=FastAPI()

@app.post('/loan-eligibility')
def check_eligibility(applicant:Applicant):
    if(applicant.age>=21 and applicant.income>=50000 and applicant.employment_status=='employed'):
        return {'eligible':True}
    else:
        return {'eligible':False} 

