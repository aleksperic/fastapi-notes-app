from fastapi import APIRouter, Depends, status
from internal.auth import authenticate_user, create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES
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
    user = authenticate_user(form_data.username, form_data.password, db)
    if user is None:
        raise CREDENTIALS_EXCEPTION
    access_token = create_access_token({'sub': user.username}, ACCESS_TOKEN_EXPIRE_MINUTES)
    return {'access_token': access_token, 'token_type': 'bearer'}