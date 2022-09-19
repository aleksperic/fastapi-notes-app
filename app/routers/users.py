from fastapi import APIRouter, Depends
from dependencies import get_token_header


router = APIRouter(
    prefix='/users',
    tags=['Users'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description':'Not found'}}
    )

@router.post('/')
def create_user():
    pass

@router.get('/{user_id}')
def get_user(post_id: int):
    pass

@router.get('/')
def get_users():
    pass

@router.put('/{user_id}')
def update_user(post_id: int):
    pass

@router.delete('/{user_id}')
def delete_user(post_id: int):
    pass