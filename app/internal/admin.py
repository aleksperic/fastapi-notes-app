from fastapi import APIRouter


router = APIRouter(
    prefix='/admin',
    tags=['Admin']
    )

@router.post('/')
def admin():
    pass