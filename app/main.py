from fastapi import FastAPI
import app.models as models, app.schemas as schemas, app.utils as utils
from app.database import engine, SessionLocal
from app.routers import post, user, auth
from app.config import settings
 
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
        

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():      
   return {"message": "welcome"}
  
