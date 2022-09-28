from fastapi import FastAPI, APIRouter, Depends
from routers import notes, users
from internal import admin, auth
from models.database import Base, engine
from dependencies import get_query_token, get_token_header
import uvicorn

# ------------------------------------------------------

# from models import schemas, database, models
# from fastapi import status, HTTPException
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
# oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

# -------------------------------------------------------


app = FastAPI(
    # dependencies=[Depends(get_query_token)]
    )
Base.metadata.create_all(engine)

app.include_router(notes.router)
app.include_router(users.router)
app.include_router(admin.router)
app.include_router(auth.router)

# ----------------------------------------------------------

# @app.post('/token')
# async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.username == form_data.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')
#     return {'access_token': user.username, 'token_type': 'bearer'}

# async def get_current_user(request: schemas.User, token: str = Depends(oauth2_schema), db: Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.username == request.username)
#     return user

# @app.get('/items')
# async def get_token(current_user: schemas.User = Depends(get_current_user)):
#     return current_user