from fastapi import APIRouter, Depends
from dependencies import get_token_header


router = APIRouter(
    prefix='/notes',
    tags=['Notes'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description':'Not found'}}
    )

@router.post('/')
def create_note():
    pass

@router.get('/{post_id}')
def get_note(post_id: int):
    pass

@router.get('/')
def get_notes():
    pass

@router.put('/{post_id}')
def update_note(post_id: int):
    pass

@router.delete('/{post_id}')
def delete_note(post_id: int):
    pass