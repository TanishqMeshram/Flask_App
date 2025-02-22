from fastapi import APIRouter , Depends , status 
from .. import schemas , db , OAuth2
from ..repository import blog
from typing import List
from sqlalchemy.orm import Session 


router = APIRouter(
    prefix="/blog",
    tags=['blogs']
) 
get_db = db.get_db

@router.get('/' , response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db) ,current_user: schemas.User=Depends(OAuth2.get_current_user) ):
    return blog.get_all(db) 

@router.post('/' ,   status_code=status.HTTP_201_CREATED )
def create(request: schemas.Blog , db : Session = Depends(get_db) , current_user: schemas.User=Depends(OAuth2.get_current_user)):
    return blog.create(request,db,current_user)

@router.get('/{id}' , status_code=status.HTTP_200_OK , response_model=schemas.ShowBlog )
def show(id: int , db: Session = Depends(get_db) , current_user: schemas.User=Depends(OAuth2.get_current_user)):
    return blog.show(id,db,current_user)

@router.delete('/{id}' , status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int,db: Session = Depends(get_db) , current_user: schemas.User=Depends(OAuth2.get_current_user)):
    return blog.destroy(id,db,current_user)

@router.put('/{id}' , status_code=status.HTTP_202_ACCEPTED )
def update(id: int , request: schemas.Blog  ,db: Session = Depends(get_db) , current_user: schemas.User=Depends(OAuth2.get_current_user)):
    return blog.update(id,request,db,current_user)