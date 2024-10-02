from pydantic import BaseModel, Field



class post(BaseModel):
    id: int
    title: str
    content: str
    published: Optional[bool] = True
    #rating: Optional[int] = None