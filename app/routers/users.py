from fastapi import APIRouter, Depends
from dependencies import get_token_header
from functions import users


router = APIRouter(
    prefix='/users',
    tags=['Users'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description':'Not found'}}
    )

@router.post('/')
def create_user():
    return users.create_user()

@router.get('/{user_id}')
def get_user(post_id: int):
    return users.get_user(post_id)

@router.get('/')
def get_users():
    return users.get_users()

@router.put('/{user_id}')
def update_user(post_id: int):
    return users.update_user(post_id)

@router.delete('/{user_id}')
def delete_user(post_id: int):
    return users.delete_user(post_id)