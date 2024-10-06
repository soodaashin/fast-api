from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

def get_current_time():
    return datetime.now()
    
class PostBase(BaseModel):
    id: int
    title: str
    content: str
    published: Optional[bool] = True
    #rating: Optional[int] = None
    created_at: datetime = get_current_time()

class PostCreate(PostBase):
    pass


class Post(BaseModel):
    id: int
    created_at: datetime = get_current_time()
    
    class Config:
        orm_mode = True