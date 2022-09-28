from fastapi import APIRouter, Form, File, UploadFile


router = APIRouter(
    prefix='/admin',
    tags=['Admin']
    )

@router.post('/')
def admin(username: str = Form(), password: str = Form()):
    return username, password

@router.post('/files')
def create_file(file: bytes = File()):
    return {'file_size': len(file)}

@router.post('/uploadfile')
def upload_file(file: UploadFile):
    return {'filename': file}
    