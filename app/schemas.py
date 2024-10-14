from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
from typing import List
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass    


class Post(BaseModel):
    
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password:str
    
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True
        
        
        
class Userlogin(BaseModel):
    email: EmailStr
    password: str