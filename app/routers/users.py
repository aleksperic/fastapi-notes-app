from fastapi import APIRouter, Depends, status
from dependencies import get_token_header
from internal import auth
from functions import users
from models import models, schemas
from models.database import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(
    prefix='/users',
    tags=['Users'],
    # dependencies=[Depends(get_token_header)],
    responses={404: {'description': 'Not found'}}
    )


@router.post('/', response_model=schemas.UserShow, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return users.create_user(request, db)

@router.get('/{username}', response_model=schemas.UserShow, status_code=status.HTTP_200_OK)
def get_user(username: str, db: Session = Depends(get_db)):
    return users.get_user(username, db)

@router.get('/', response_model=List[schemas.UserShow], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return users.get_users(db)

@router.put('/{username}', status_code=status.HTTP_202_ACCEPTED)
def update_user(username: str, request: schemas.UserUpdate, db: Session = Depends(get_db)):
    return users.update_user(username, request, db)

@router.delete('/{username}', status_code=status.HTTP_410_GONE)
def delete_user(username: str, db: Session = Depends(get_db)):
    return users.delete_user(username, db)

@router.get('/me', response_model=schemas.UserShow, status_code=status.HTTP_200_OK)
def my_info(current_user: schemas.UserShow = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    return current_user