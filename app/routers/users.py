from fastapi import APIRouter, Depends, status
from internal.auth import get_current_user, login_auth
from functions import users
from models import schemas
from models.database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Users'],
    responses={404: {'description': 'Not found'}}
    )

@router.get('/me', response_model=schemas.UserShow, status_code=status.HTTP_200_OK)
def my_info(current_user: schemas.UserShow = Depends(get_current_user)):
    return current_user

@router.post('/sign_up', response_model=schemas.UserShow, status_code=status.HTTP_201_CREATED)
def sign_up(request: schemas.User, db: Session = Depends(get_db)):
    return users.sign_up(request, db)

@router.post('/login', response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return login_auth(form_data, db)