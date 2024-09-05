from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()


class post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating: Optional[int] = None

while True:
    try:
        conn = psycopg2.connect(host= 'localhost', database='FastAPI', user="postgres", password="sood",  cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection was sucessfull !")
        
        break
        
    except Exception as error:
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
    return {"message": "welcome to fast new fast api"}


@app.get("/posts")
def get_posts():
    return{"data" : my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def createposts(post : post):
    
    post_dict = post.dict()
    post_dict["id"] = randrange(0 , 100000000)
    
    my_posts.append(post_dict)
    return {"data : " :  post_dict}


@app.get("/posts/{id}")
def get_post(id : int, response: Response):
    # print(id)
    
    post = findpost(id)
    
    if not post:
        
        return{"post detail" : post}
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exists")
        
    #     response.status_code = status.HTTP_404_NOT_FOUND
    
    # return{f"this post with id {id} was not found in database"}
    # return {"post_detail" : f"here is post{id}"}
    
 
 
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteposts(id:int):
    
    index = find_post(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =  f"post with id {id}  does not exist")
    
    my_posts.pop(index)
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    #return{"message" : "post was deleted"}
    
    
    
@app.put("/posts/{id}")
def updatepost(id:int, post:post):
    
    index = find_post(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =  f"post with id {id}  does not exist")
    
   # print(post)
   
    post_dict = post.dict()
    post_dict["id"] = id
    
    my_posts [index] = post_dict
    
    return {"data" : post_dict}
    
    return{"updated post"}