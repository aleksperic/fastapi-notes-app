from models import models, schemas
from models.database import get_db
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from environs import Env
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


env = Env()
env.read_env()
SECRET_KEY = env.str('SECRET_KEY')
ALGORITHM = env.str('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = env.int('ACCESS_TOKEN_EXPIRE_MINUTES')

router = APIRouter(
        prefix='',
        tags=['Authentifications']
        )

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

CREDENTIALS_EXCEPTION = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
        )

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_from_db(username: str, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        return False
    return user

def authenticate_user(username: str, password: str, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise CREDENTIALS_EXCEPTION
    if not verify_password(password, user.password):
        raise CREDENTIALS_EXCEPTION
    return user

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(expires_delta)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise CREDENTIALS_EXCEPTION
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise CREDENTIALS_EXCEPTION
    user = get_user_from_db(token_data.username, db)
    if not user:
        raise CREDENTIALS_EXCEPTION
    return user

# @router.post('/login', response_model=schemas.Token)
def login_auth(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if user is None:
        raise CREDENTIALS_EXCEPTION
    access_token = create_access_token({'sub': user.username}, ACCESS_TOKEN_EXPIRE_MINUTES)
    return {'access_token': access_token, 'token_type': 'bearer'}