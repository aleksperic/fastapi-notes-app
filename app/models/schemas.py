from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class UserBase(BaseModel):

    class Config():
        orm_mode = True
    

class User(UserBase):

    username: str
    password: str
    email: str

class UserUpdate(UserBase):
    password: str
    email: str


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

    created: datetime
    active: bool = True

class NoteUpdate(NoteBase):
    title: str
    body: str = Field(title="The description of the item", max_length=300)
    created: datetime

class UserShow(UserBase):

    id: int
    username: str
    email: str
    notes: List[NoteShow] | None
    class Config():
        orm_mode=True