from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel, Field
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class post(BaseModel):
    id: int
    title: str
    content: str
    published: Optional[bool] = True
    rating: Optional[int] = None

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
         


@app.get("/")
async def root():      
   return {"message": "welcome"}


@app.get("/posts")
def get_posts():
    cursor.execute("""Select * from posts""")
    posts = cursor.fetchall()
    #print(posts)
    return{"data" : posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: post):
    
    cursor.execute("""INSERT INTO posts (id, title, content, published) VALUES (%s, %s, %s, %s) RETURNING *""",(post.id, post.title, post.content, post.published))
    
    created_post = cursor.fetchone()
    
    conn.commit()
    #print(create_post)
    return {"data": created_post}

@app.get("/posts/{id}")
def get_post(id : int):
    
    cursor.execute("""Select * from posts where id = %s """, (str(id)))
    
    posts = cursor.fetchone()
    
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exists")
    return{"data" : posts}
 
 
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteposts(id:int):
    
    
    cursor.execute(""" delete from posts where id  = %s returning * """, (str(id)))
    
    deleted_posts  = cursor.fetchone()
    
    conn.commit()
    #index = find_post(id)
    
    if deleted_posts == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =  f"post with id {id}  does not exist")
    
    #my_posts.pop(index)
     
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    #return{"message" : "post was deleted"}
    
    
    
@app.put("/posts/{id}")
def updatepost(id:int, post:post):
    
    
    cursor.execute(""" update posts set title = %s,  content = %s, published = %s  returning * """,(post.title, post.content, post.published))
    
    updated_post =  cursor.fetchone()
    
    
    conn.commit()
    #index = find_post(id)
    
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =  f"post with id {id}  does not exist")
    
   # print(post)
   

    return{"updated post" : updated_post}



@app.get('/sqlalchemy')
def testposts(db: Session = Depends(get_db)):
    
    return{"data" : "sucess"}