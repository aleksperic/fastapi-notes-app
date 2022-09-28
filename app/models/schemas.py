from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import List


class UserBase(BaseModel):

    class Config():
        orm_mode = True
    
class User(UserBase):

    username: str
    password: str
    email: EmailStr

class UserUpdate(UserBase):
    password: str
    email: EmailStr

class NoteBase(BaseModel):

    class Config():
        orm_mode = True

class NoteShow(NoteBase):

    id: int
    title: str
    body: str
    created: datetime
    active: bool
    user_id: int

class Note(NoteBase):

    body: str | None = Field(title="The description of the note", default=None, max_length=300)
    created: datetime
    active: bool = True

class NoteUpdate(NoteBase):
    title: str
    body: str = Field(title="The description of the note", max_length=300)
    created: datetime

class UserShow(UserBase):

    id: int
    username: str
    email: EmailStr
    notes: List[NoteShow] | None
    class Config():
        orm_mode=True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None