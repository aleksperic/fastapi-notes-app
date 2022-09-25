from fastapi import APIRouter, Depends, status, Body
from dependencies import get_token_header
from functions import notes
from models import models, schemas
from models.database import get_db
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime


router = APIRouter(
    prefix='/notes',
    tags=['Notes'],
    #dependencies=[Depends(get_token_header)],
    responses={404: {'description':'Not found'}}
    )

@router.post('/', response_model=schemas.NoteShow, status_code=status.HTTP_201_CREATED)
def create_note(request: schemas.Note, user_id: int, title: str, body: str, db: Session = Depends(get_db)):
    return notes.create_note(request, user_id, title, body, db)

@router.get('/{id}', response_model=schemas.NoteShow, status_code=status.HTTP_200_OK)
def get_note(id: int, db: Session = Depends(get_db)):
    return notes.get_note(id, db)

@router.get('/', response_model=List[schemas.NoteShow], status_code=status.HTTP_200_OK)
def get_notes(db: Session = Depends(get_db)):
    return notes.get_notes(db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_note(id: int, active: bool, request: schemas.NoteUpdate, db: Session = Depends(get_db)):
    return notes.update_note(id, active, request, db)

@router.delete('/{id}', status_code=status.HTTP_410_GONE)
def delete_note(id: int, db: Session = Depends(get_db)):
    return notes.delete_note(id, db)