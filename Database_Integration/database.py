from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker


db_url='sqlite:///./test.db'

engine=create_engine(db_url,connect_args={'check_same_thread':False})

session_local=sessionmaker(engine,autoflush=False,autocommit=False)
Base=declarative_base()