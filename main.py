from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating: Optional[int] = None
 

@app.get("/")
async def root():
    return {"message": "welcome to fast new fast api"}


@app.get("/posts")
def get_posts():
    return{"data:" "this is your post"}


@app.post("/createposts")
def createposts(post : post):
    print(post.rating)
    print(post.dict())
    return {"data : " :  post}