from pydantic import BaseModel
from fastapi import UploadFile, File

class UserLogin(BaseModel):
    email: str
    password: str

class UserSignUp(BaseModel):
    email: str
    password: str

# Updated file upload model
class FileUpload(BaseModel):
    filename: str
    # FastAPI's UploadFile is used to handle file uploads
    file: UploadFile  # This will be an actual file object, not just bytes
