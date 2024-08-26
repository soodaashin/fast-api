from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "welcome to fast new fast api"}


@app.get("/posts")
def get_posts():
    return{"data:" "this is your post"}


@app.post("/createposts")
def createposts(data: dict = Body(...) ):
    print(data)
    return {"new post" : f"title {data['title']} content : {data['content']}"}
 
