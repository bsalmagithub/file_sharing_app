from fastapi import APIRouter, Depends, HTTPException
from db import get_db
from models import User, FileRecord
from utils import encrypt_url

router = APIRouter()

@router.post("/sign-up")
def sign_up(client_user: UserSignUp, db=Depends(get_db)):
    verification_link = encrypt_url(client_user.email)
    new_user = User(email=client_user.email, hashed_password=hash_password(client_user.password), user_type="client")
    db.add(new_user)
    db.commit()
    return {"verification_link": verification_link}

@router.post("/email-verify")
def email_verify(verification_link: str, db=Depends(get_db)):
    return {"message": "Email verified successfully"}

@router.post("/login")
def login_client_user(user_login: UserLogin, db=Depends(get_db)):
    return {"session_token": "generated_token"}

@router.get("/list-files")
def list_files(session_token: str, db=Depends(get_db)):
    if not verify_session(session_token, "client"):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    files = db.query(FileRecord).all()
    return [{"filename": file.filename, "id": file.id} for file in files]

@router.get("/download-file/{file_id}")
def download_file(file_id: int, session_token: str, db=Depends(get_db)):
    if not verify_session(session_token, "client"):
        raise HTTPException(status_code=403, detail="Unauthorized")
    
    download_link = encrypt_url(f"file_id:{file_id}")
    return {"download-link": f"https://example.com/download-file/{download_link}", "message": "success"}
