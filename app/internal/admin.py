from fastapi import APIRouter, Form


router = APIRouter(
    prefix='/admin',
    tags=['Admin']
    )

@router.post('/')
def admin(username: str = Form(), password: str = Form()):
    return username, password