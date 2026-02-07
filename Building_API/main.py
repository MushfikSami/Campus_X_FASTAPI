
from fastapi import FastAPI,HTTPException
from typing import List 
from models_val import Employee

employee_db:List[Employee]=[]

app=FastAPI()

app.get('/employees',response_model=List[Employee])
def get_employees():
    return employee_db


app.get('/employees/{emp_id}',response_model=Employee)
def get_employee(emp_id:int):
    for index,emp in enumerate(employee_db):
        if emp.id==emp_id:
            return employee_db[index]
    raise HTTPException(status_code=404,detail='Employee not found')


app.post('/add_employee',response_model=Employee)
def add_employee(new_emp:Employee):
    for index,emp in enumerate(employee_db):
        if emp.id==new_emp.id:
            raise HTTPException(status_code=400,detail='Employee Already Exists')
    employee_db.append(new_emp)
    return new_emp


app.put('/update_employee/{emp_id}',response_model=Employee)
def update_employee(emp_id:int,updated_emp:Employee):
    for index,emp in enumerate(employee_db):
        if emp.id==emp_id:
            employee_db[index]=update_employee
            return update_employee
    raise HTTPException(status_code=404,detail='Employee not found')


app.delete('/delete_employee/{emp_id}',response_model=Employee)
def delete_employee(emp_id:int):
    for index,emp in enumerate(employee_db):
        if emp.id==emp_id:
            del employee_db[index]
            return {'message':'Employee Deleted Successfully'}
    raise HTTPException(status_code=404,detail='Employee not found')    
