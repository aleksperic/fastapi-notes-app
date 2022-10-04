from fastapi import FastAPI
from routers import notes, users
from internal import admin, auth
from models.database import Base, engine


app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(notes.router)
app.include_router(users.router)
app.include_router(admin.router)
app.include_router(auth.router)