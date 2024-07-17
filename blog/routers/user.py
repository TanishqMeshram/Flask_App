from fastapi import APIRouter , Depends 
from .. import schemas , db
from sqlalchemy.orm import Session 
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['users']
) 
get_db = db.get_db


@router.post('/' , response_model=schemas.ShowUser )
def create_user(request: schemas.User , db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}' , response_model=schemas.ShowUser )
def get_user(id:int , db: Session = Depends(get_db)):
    return user.getUser(id,db)