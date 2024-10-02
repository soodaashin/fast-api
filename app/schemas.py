from pydantic import BaseModel, Field
from typing import Optional


    
class PostBase(BaseModel):
    id: int
    title: str
    content: str
    published: Optional[bool] = True
    #rating: Optional[int] = None


class PostCreate(PostBase):
    pass


class Post(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True
    
    class Config:
        orm_mode = True