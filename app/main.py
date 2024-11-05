from fastapi import FastAPI
from . import models, schemas, utils
from .database import engine, SessionLocal
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# while True:
    
#     try:
#         conn = psycopg2.connect(host='localhost', database='FastAPI', user ='postgres', password='sood', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection sucessfull")
        
#         break
        
#     except  Exception as error:
#         print("connection failed")
        
#         print("Error", error)
        
#         time.sleep(3)
        

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():      
   return {"message": "welcome"}
  
