from fastapi import APIRouter, Depends, UploadFile, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models import FileRecord, UserLogin  # Make sure UserLogin is imported
import os

router = APIRouter()

# Endpoint for Ops user login
@router.post("/login")
def login_ops_user(user_login: UserLogin, db: Session = Depends(get_db)):
    # Logic for validating the Ops user login can be added here
    # In real-life scenarios, the user login would authenticate against a DB
    if user_login.email == "ops@example.com" and user_login.password == "password":  # Example validation
        return {"session_token": "generated_token"}  # Token generation logic should be here
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Endpoint for file upload
@router.post("/upload-file")
async def upload_file(file: UploadFile, session_token: str, db: Session = Depends(get_db)):
    # Validate file type
    valid_content_types = [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",  # DOCX
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",  # PPTX
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  # XLSX
    ]
    if file.content_type not in valid_content_types:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Make sure the 'files' directory exists
    file_location = os.path.join("files", file.filename)
    os.makedirs(os.path.dirname(file_location), exist_ok=True)

    # Save the file to the file system
    with open(file_location, "wb") as f:
        f.write(await file.read())  # Asynchronous file read and write

    # Store the file record in the database
    file_record = FileRecord(filename=file.filename, user_id=1)  # Replace user_id with actual user ID from session
    db.add(file_record)
    db.commit()

    # Return success message
    return {"message": "File uploaded successfully", "filename": file.filename}
