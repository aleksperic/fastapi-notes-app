from models import models, schemas, database
from fastapi import HTTPException, status

def create_user(user, db):
    new_user = models.User(username=user.username, password=user.password, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(username, db):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {username} not found')
    return user
    
def get_users(db):
    users = db.query(models.User).all()
    return users

def update_user(username, request, db):
    user = db.query(models.User).filter(models.User.username == username)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {username} not found')
    user.update({'password': request.password, 'email': request.email}, synchronize_session=False)
    db.commit()
    return f'User {username} updated!'

def delete_user(username, db):
    user = db.query(models.User).filter(models.User.username == username)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {username} not found')
    user.delete(synchronize_session=False)
    db.commit()
    return f'User - {username} deleted!'