from fastapi import APIRouter, Depends, status
from dependencies import get_token_header
from functions import users
from models import models, schemas
from models.database import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(
    prefix='/users',
    tags=['Users'],
    # dependencies=[Depends(get_token_header)],
    responses={404: {'description':'Not found'}}
    )


@router.post('/', response_model=schemas.UserShow, status_code=status.HTTP_201_CREATED)
def create_user(username: str, password: str, email: str, db: Session = Depends(get_db)):
    return users.create_user(username,password, email, db)

@router.get('/{username}', response_model=schemas.UserShow, status_code=status.HTTP_200_OK)
def get_user(username: str, db: Session = Depends(get_db)):
    return users.get_user(username, db)

@router.get('/', response_model=List[schemas.UserShow], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return users.get_users(db)

@router.put('/{username}', response_model=schemas.UserShow, status_code=status.HTTP_202_ACCEPTED)
def update_user(username: str, request: schemas.UserUpdate, db: Session = Depends(get_db)):
    return users.update_user(username, request, db)

@router.delete('/{username}', status_code=status.HTTP_410_GONE)
def delete_user(username: str, db: Session = Depends(get_db)):
    return users.delete_user(username, db)