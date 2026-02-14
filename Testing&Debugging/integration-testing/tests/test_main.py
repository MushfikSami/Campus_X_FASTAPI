from fastapi.testclient import TestClient 
from app.main import app 

client=TestClient(app)

def test_eligibility_pass():
    payload={
        "age": 25,
        "income": 60000,
        "employment_status": "employed"
    }
    response=client.post("/loan-eligibility", json=payload)
    assert response.status_code==200
    assert response.json()=={'eligible': True}


def test_eligibility_fail():
    payload={
        "age": 17,
        "income": 30000,
        "employment_status": "unemployed"
    }
    response=client.post("/loan-eligibility", json=payload)
    assert response.status_code==200
    assert response.json()=={'eligible': False}