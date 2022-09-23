from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String)

    posts = relationship('Note', back_populates='users')

class Note(Base):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    titile = Column(String)
    body = Column(String)
    active = Column(Boolean(create_constraint=True))
    created = Column(DateTime(timezone=True))
    user_id = Column(Integer, ForeignKey('users.id'))

    users = relationship('User', back_populates='posts')