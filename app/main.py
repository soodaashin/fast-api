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
         


@app.get("/")
async def root():      
   return {"message": "welcome"}


@app.get("/posts", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""Select * from Post""")
    # posts = cursor.fetchall()
    #print(posts)
    
    posts = db.query(models.post).all() 
    
    return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
        
    new_post =  models.post(**post.dict())
    
    
    db.add(new_post) 
    db.commit()
    
    db.refresh(new_post)
    
    return new_post

    
    

@app.get("/posts/{id}", response_model=schemas.Post)
def get_post(id : int, db: Session = Depends(get_db)):
    
    
    post = db.query(models.post).filter(models.post.id == id).first()
     
    if post == None:
        return {"error": "Post not found"}  # Handle the case where the post is not found

    return post 
    
    #cursor.execute("""Select * from posts where id = %s """, (str(id)))
    
    # posts = cursor.fetchone()
    
    # if not posts:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exists")
    # return{"data" : posts}
 
 
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteposts(id:int, db: Session = Depends(get_db)):
    
    
    post = db.query(models.post).filter(models.post.id == id)

    
    
    # cursor.execute(""" delete from posts where id  = %s returning * """, (str(id)))
    
    # deleted_posts  = cursor.fetchone()
    
    # conn.commit()
    #index = find_post(id)
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =  f"post with id {id}  does not exist")
    
    #my_posts.pop(index)
    
    post.delete(synchronize_session=False   )
    
    db.commit()
     
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    #return{"message" : "post was deleted"}
    
    
    
    
@app.put("/posts/{id}", response_model=schemas.Post)
def updatepost(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    # Query to find the post by ID
    post_query = db.query(models.post).filter(models.post.id == id)
    post = post_query.first() 

    # Check if the post exists
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
    
    # Update the post
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    # Return the updated post
    return post
    #print(updated_post.dict())




# @app.get('/sqlalchemy')
# def testposts(db: Session = Depends(get_db)):
    
     
#     posts = db.query(models.Post).all()
#     return{"data" : posts}


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    
    #hass password
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
  
    new_user =  models.User(**user.dict())

    db.add(new_user) 
    db.commit()
    
    db.refresh(new_user)

    return new_user



@app.get('/users/{id}')
def get_user(id : int, db: Session = Depends(get_db)):
        user = db.query(models.User).filter(models.User.id == id).first()
        
        if not user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"user with {id} does not exist")
        return user
        