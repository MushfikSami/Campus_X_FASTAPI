from sqlalchemy import Column,String,Integer
from database import Base 

class Employee(Base):
    __tablename__='employees'
    ID=Column(Integer,index=True,primary_key=True)
    name=Column(String,index=True)
    department=Column(String,index=True)
    email=Column(String,unique=True,index=True)