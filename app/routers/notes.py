from fastapi import APIRouter, Depends, status, Query, Path
from fastapi.security import OAuth2PasswordBearer
from dependencies import get_token_header
from functions import notes
from internal import auth
from models import models, schemas
from models.database import get_db
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime


router = APIRouter(
                    prefix='/notes',
                    tags=['Notes'],
                    responses={404: {'description': 'Not found'}}
                 )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get('/{username}', response_model=List[schemas.UserPublicNotes], status_code=status.HTTP_200_OK)
def get_public_notes(   username: str,
                        db: Session = Depends(get_db)
                    ):
    return notes.get_public_notes(username, db)

@router.post('/', response_model=schemas.NoteShow, status_code=status.HTTP_201_CREATED)
def create_note(request: schemas.Note,
                current_user: schemas.UserShow = Depends(auth.get_current_user),
                db: Session = Depends(get_db)
                ):
    return notes.create_note(request, current_user, db)

@router.get('/note/{id}', response_model=schemas.NoteShow, status_code=status.HTTP_200_OK)
def get_note(   id: int,
                db: Session = Depends(get_db),
                current_user: schemas.UserShow = Depends(auth.get_current_user)
            ):
    return notes.get_note(id, db, current_user)

@router.get('/', response_model=List[schemas.NoteShow], status_code=status.HTTP_200_OK)
def get_notes(  db: Session = Depends(get_db),
                current_user: schemas.UserShow = Depends(auth.get_current_user)
                ):
    return notes.get_notes(db, current_user)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_note(id: int,
                public: bool,
                request: schemas.NoteUpdate,
                db: Session = Depends(get_db),
                current_user: schemas.UserShow = Depends(auth.get_current_user)
                ):
    return notes.update_note(id, public, request, db, current_user)

@router.delete('/{id}', status_code=status.HTTP_410_GONE)
def delete_note(id: int,
                db: Session = Depends(get_db),
                current_user: schemas.UserShow = Depends(auth.get_current_user)
                ):
    return notes.delete_note(id, db, current_user)