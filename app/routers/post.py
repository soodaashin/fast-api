import app.models as models, app.schemas as schemas, app.utils as utils, app.oauth2 as oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import engine, SessionLocal, get_db
from typing import Optional, List


router = APIRouter(
    prefix="/posts",
    tags=["Post"]
)


@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit:int = 10, skip:int = 0, search:Optional[str]=""):
    # cursor.execute("""Select * from Post""")
    # posts = cursor.fetchall()
    #print(posts)
    
    print(limit)
    posts = db.query(models.post).filter(models.post.title.contains(search)).limit(limit).offset(skip).all()
    
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
        
    print(current_user.id) 
    print(current_user.email)
    
    new_post =  models.post(owner_id  = current_user.id, **post.dict())
    
    
    db.add(new_post) 
    db.commit()
    
    db.refresh(new_post)
    
    return new_post

    
    

@router.get("/{id}", response_model=schemas.Post)
def get_post(id : int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    
    
    print(limit) 
    post = db.query(models.post).filter(models.post.id == id).first()
     
     
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, details="not authorized to perform requested action")
     
    if post == None:
        return {"error": "Post not found"}  # Handle the case where the post is not found

    return post 
    
    #cursor.execute("""Select * from posts where id = %s """, (str(id)))
    
    # posts = cursor.fetchone()
    
    # if not posts:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exists")
    # return{"data" : posts}
 
 
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteposts(id:int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    
    post_query = db.query(models.post).filter(models.post.id == id)

    
    
    # cursor.execute(""" delete from posts where id  = %s returning * """, (str(id)))
    
    # deleted_posts  = cursor.fetchone()
    
    # conn.commit()
    #index = find_post(id)
   
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =  f"post with id {id}  does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, details="not authorized to perform requested action")
    
    
    #my_posts.pop(index)
    
    post_query.delete(synchronize_session=False)
    
    db.commit()
     
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    #return{"message" : "post was deleted"}
    
    
    
    
@router.put("/posts/{id}", response_model=schemas.Post)
def updatepost(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # Query to find the post by ID
    post_query = db.query(models.post).filter(models.post.id == id)
    post = post_query.first() 

    # Check if the post exists
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
    
    
    if post.owner_id != oauth2.current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, details="not authorized to perform requested action")
    
    
    # Update the post
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    # Return the updated post
    return post
    #print(updated_post.dict())




# @app.get('/sqlalchemy')
# def testposts(db: Session = Depends(get_db)):
    
     
#     posts = db.query(models.Post).all()
#     return{"data" : posts}
