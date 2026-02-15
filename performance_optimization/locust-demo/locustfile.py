import json 
from locust import HttpUser, task, between 

class APIUser(HttpUser):
    wait_time=between(1,2)

    @task
    def call_predict(self):
        payload={
            'feature1':2,
            'feature2':3
        }
        headers={'Content-type':'application/json'}
        self.client.post('/predict',data=json.dumps(payload),headers=headers)

    @task(1) 
    def call_root(self):
        self.client.get('/')    