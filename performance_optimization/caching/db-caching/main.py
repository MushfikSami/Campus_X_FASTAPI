import sqlite3
import json 
import redis 
import hashlib
from fastapi import FastAPI 
from pydantic import BaseModel 

app=FastAPI()
redis_client=redis.Redis(host='localhost',port=6379,db=0)

def get_db_connection():
    conn=sqlite3.connect('db.sqlite3')
    conn.row_factory=sqlite3.Row 
    return conn

def init_db():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute(
        '''
        create table if not exists users(
        id integer primary key,
        name text not null,
        age integer
        )

        '''
    )
    cursor.execute('insert into users (id,name,age) values (1,"Mushfik",20)')
    cursor.execute('insert into users (id,name,age) values (2,"Sami",22)')
    cursor.execute('insert into users (id,name,age) values (3,"Siam",25)')
    conn.commit()
    conn.close()
init_db()


class UserQuery(BaseModel):
    user_id:int 

def make_cache_key(user_id:int):
    raw=f'user:{user_id}'
    return hashlib.sha256(raw.encode()).hexdigest()


@app.post('/get_user')
def get_user(query:UserQuery):
    key=make_cache_key(query.user_id)
    cache_result=redis_client.get(key)
    if cache_result:
        return json.loads(cache_result)
    
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute('select * from user where id=?',(query.user_id))
    row=cursor.fetchone()
    cursor.close()

    result={'id':row[id],'name':row['name'],'áge':row['age']}

    redis_client.setex(key,6000,json.dumps(result))
    return result