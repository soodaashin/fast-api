from fastapi import FastAPI
import app.models as models, app.schemas as schemas, app.utils as utils
from app.database import engine, SessionLocal
from app.routers import post, user, auth
from app.config import Settings
from fastapi.middleware.cors import CORSMiddleware

 
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
        

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():      
   return {"message": "welcome"}
  
