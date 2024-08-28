from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating: Optional[int] = None
    
 
 
my_posts = [{"title" : "title of post", "content": "content of post" , "id": 1}, {"title" : "second post", "content": "new second post", "id":2}] 

def findpost(id):
    
    for p in my_posts:
        if p["id"]  == id:
            return p


@app.get("/")
async def root():
    return {"message": "welcome to fast new fast api"}


@app.get("/posts")
def get_posts():
    return{"data" : my_posts}


@app.post("/posts")
def createposts(post : post):
    
    post_dict = post.dict()
    post_dict["id"] = randrange(0 , 100000000)
    
    my_posts.append(post_dict)
    return {"data : " :  post_dict}


@app.get("/posts/{id}")
def get_post(id : int):
    # print(id)
    
    post = findpost(id)
    return{"post detail" : post}
    
    # return {"post_detail" : f"here is post{id}"}
    
    
    
    