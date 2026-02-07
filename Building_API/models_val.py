from pydantic import BaseModel,Field,StrictInt
from typing import Optional

class Employee(BaseModel):
    id:int=Field(...,gt=0)
    name:str=Field(...,gt=3,lt=30)
    department:str=Field(...,gt=3,lt=30)
    age:Optional[StrictInt]=Field(...,ge=18)