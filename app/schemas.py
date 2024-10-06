from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, TIMESTAMP, text
from sqlalchemy.orm import Mapped, mapped_column


Base = declarative_base()

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
    
    __tablename__ = "Posts"
    
    id: int
    created_at: datetime = get_current_time()
    
    class Config:
        orm_mode = True
    
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
