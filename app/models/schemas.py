from pydantic import BaseModel, Field


class UserBase(BaseModel):

    class Config():
        orm_mode = True

class UserShow(UserBase):

    id: int
    username: str
    email: str
    

class User(UserBase):

    username: str
    password: str
    email: str

class UserUpdate(UserBase):
    password: str
    email: str


class NoteBase(BaseModel):
    
    title: str
    body: str

    class Config():
        orm_mode = True

class NoteShow(NoteBase):

    active: str
    create: str

class Note(NoteBase):

    id: int
    active: str