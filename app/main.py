from fastapi import FastAPI, APIRouter, Depends
from routers import notes, users
from internal import admin
from models.database import Base, engine
from dependencies import get_query_token, get_token_header


app = FastAPI(
    # dependencies=[Depends(get_query_token)]
    )
Base.metadata.create_all(engine)

app.include_router(notes.router)
app.include_router(users.router)
app.include_router(admin.router)