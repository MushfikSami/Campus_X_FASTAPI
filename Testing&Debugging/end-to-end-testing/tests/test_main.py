from fastapi.testclient import TestClient
from app.main import app 
 

client=TestClient(app)

def test_eligible_true():
    response=client.post('/loan-eligibility', json={
        "age": 30,
        "income": 60000,
        'employment_status': 'employed'})
    assert response.status_code == 200
    assert response.json() == {"eligible": True}


def test_eligible_false():
    response=client.post('/loan-eligibility', json={
        "age": 20,
        "income": 40000,
        'employment_status': 'unemployed'})
    assert response.status_code == 200
    assert response.json() == {"eligible": False}
