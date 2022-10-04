from fastapi import APIRouter, Depends, status, Form
from functions import users
from models import schemas
from models.database import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(
    tags=['Admin']
    )

@router.post('/')
def admin(username: str = Form(), password: str = Form()):
    return username, password

@router.get('/user/{username}', response_model=schemas.UserShow, status_code=status.HTTP_200_OK)
def get_user(username: str, db: Session = Depends(get_db)):
    return users.get_user(username, db)

@router.get('/users', response_model=List[schemas.UserShow], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return users.get_users(db)

@router.put('/user/{username}', status_code=status.HTTP_202_ACCEPTED)
def update_user(username: str, request: schemas.UserUpdate, db: Session = Depends(get_db)):
    return users.update_user(username, request, db)

@router.delete('/user/{username}', status_code=status.HTTP_410_GONE)
def delete_user(username: str, db: Session = Depends(get_db)):
    return users.delete_user(username, db)