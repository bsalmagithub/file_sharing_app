import hashlib
import os
import base64

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def encrypt_url(data: str) -> str:
    return base64.urlsafe_b64encode(data.encode()).decode()

def verify_session(session_token: str, user_type: str) -> bool:
    # Dummy session verification
    return True
