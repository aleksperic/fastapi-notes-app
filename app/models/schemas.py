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


class PostBase(BaseModel):
    
    title: str
    body: str

    class Config():
        orm_mode = True

class PostCreate(PostBase):

    active: str
    create: str

class Post(PostBase):

    id: int
    active: str
    class Config():
        orm_mode = True
