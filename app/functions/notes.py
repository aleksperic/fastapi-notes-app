from models import models, schemas, database
from fastapi import HTTPException, status

def create_note(request, user_id, title, body, db):
    new_note = models.Note(user_id=user_id, title=title, body=body, active=request.active, created=request.created)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

def get_note(id, db):
    note = db.query(models.Note).filter(models.Note.id == id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note {id} not found')
    return note
    
def get_notes(db):
    notes = db.query(models.Note).all()
    return notes

def update_note(id, active, request, db):
    note = db.query(models.Note).filter(models.Note.id == id)
    if not note.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note {id} not found')
    note.update({'title': request.title, 'body': request.body, 'active': active}, synchronize_session=False)
    db.commit()
    return f'Note id: {id} updated!'

def delete_note(id, db):
    note = db.query(models.Note).filter(models.Note.id == id)
    if not note.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note {id} not found')
    note.delete(synchronize_session=False)
    db.commit()
    return f'Note id: {id} deleted!'