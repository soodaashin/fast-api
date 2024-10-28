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


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True


class Post(BaseModel):
    
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
        
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password:str
    
        
        
        
class Userlogin(BaseModel):
    email: EmailStr
    password: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
    
class TokenData(BaseModel):
    id: Optional[str]