from fastapi import APIRouter, Depends
from dependencies import get_token_header
from functions import notes


router = APIRouter(
    prefix='/notes',
    tags=['Notes'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description':'Not found'}}
    )

@router.post('/')
def create_note():
    return notes.create_note()

@router.get('/{post_id}')
def get_note(post_id: int):
    return notes.get_note(note_id)

@router.get('/')
def get_notes():
    return notes.get_notes()

@router.put('/{post_id}')
def update_note(post_id: int):
    return notes.update_note(note_id)

@router.delete('/{post_id}')
def delete_note(post_id: int):
    return notes.delete_note(note_id)