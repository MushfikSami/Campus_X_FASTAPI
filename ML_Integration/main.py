from typing import List
from fastapi import FastAPI 
from schemas import InputSchema, OutputSchema
from predict import make_prediction,make_batch_prediction


app=FastAPI()

@app.get('/')
def index():
    return {"message":"Welcome to the House Price Prediction API"}



@app.post('/prediction',response_model=OutputSchema)
def predict_price(user_input:InputSchema):
    predicted=make_prediction(user_input.model_dump())
    return OutputSchema(predicted_price=predicted)



@app.post('/batch_prediction',response_model=List[OutputSchema])
def batch_predict(user_input:List[InputSchema]):
    predictions=make_batch_prediction([item.model_dump() for item in user_input])
    return [OutputSchema(predicted_price=pred) for pred in predictions]