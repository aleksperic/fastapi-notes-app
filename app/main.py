from fastapi import FastAPI, APIRouter, Depends
from routers import notes, users
from internal import admin, auth
from models.database import Base, engine
from dependencies import get_query_token, get_token_header


app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(notes.router)
app.include_router(users.router)
app.include_router(admin.router)
app.include_router(auth.router)