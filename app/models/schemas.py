from pydantic import BaseModel


class UserBase(BaseModel):

    username: str
    password: str
    email: str

class UserCreate(UserBase):

    usename: str
    password: str

class User(UserBase):
        
    id: int
    username: str
    email: str

    class Config():
        orm_mode = True


class PostBase(BaseModel):
    
    title: str
    body: str

class PostCreate(PostBase):

    titile: str
    body: str
    active: str
    create: str

class Post(PostBase):

    id: int
    title: str
    active: str

    class Config():
        orm_mode = True