from fastapi import FastAPI 
from .logic import is_eligible_for_loan
from pydantic import BaseModel 

app=FastAPI()

class Applicant(BaseModel):
    age:int
    income:float
    employment_status:str 


@app.post('/loan-eligibility')
def check_eligibility(applicant:Applicant):
    eligible=is_eligible_for_loan(applicant.age,applicant.income,applicant.employment_status)    
    return {'eligible':eligible}