from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel, Field
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, get_db
from .routers import post, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    
    try:
        conn = psycopg2.connect(host='localhost', database='FastAPI', user ='postgres', password='sood', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection sucessfull")
        
        break
        
    except  Exception as error:
        print("connection failed")
        
        print("Error", error)
        
        time.sleep(3)
        
        
 
my_posts = [{"title" : "title of post", "content": "content of post" , "id": 1}, {"title" : "second post", "content": "new second post", "id":2}] 

def findpost(id):
    
    for p in my_posts:
        if p["id"]  == id:
            return p
        
        
def find_post(id):
    for i , p in enumerate(my_posts):
        if p['id'] == id:
            return id
         

app.include_router(post.router)


@app.get("/")
async def root():      
   return {"message": "welcome"}

