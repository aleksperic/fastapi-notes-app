from models import models
from fastapi import HTTPException, status


def get_public_notes(db):
    notes = db.query(models.Note).filter(models.Note.public == True, models.Note.active == True)
    return list(notes)

def create_note(request, current_user, db):
    new_note = models.Note(user_id=current_user.id, title=request.title, body=request.body, active=request.active, public=request.public, created=request.created)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

def get_note(id, db, user):
    note = db.query(models.Note).filter(models.Note.user_id == user.id).filter(models.Note.id == id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note {id} not found')
    return note
    
def get_notes(db, user):
    notes = db.query(models.Note).filter(models.Note.user_id == user.id)
    return list(notes)

def update_note(id, public, request, db, user):
    note = db.query(models.Note).filter(models.Note.user_id == user.id).filter(models.Note.id == id)
    if not note.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note {id} not found')
    note.update({'title': request.title, 'body': request.body, 'active': request.active, 'public': public}, synchronize_session=False)
    db.commit()
    return f'Note id: {id} updated!'

def delete_note(id, db, user):
    note = db.query(models.Note).filter(models.Note.user_id == user.id).filter(models.Note.id == id)
    if not note.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note {id} not found')
    note.delete(synchronize_session=False)
    db.commit()
    return f'Note id: {id} deleted!'