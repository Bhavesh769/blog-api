from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.auth import decode_access_token
from app import models


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_db():
    db = SessionLocal()
    try:
        yeild db
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNATHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},         
    )

    payload = decode_access_token(token)
    if payload is None:
        raise credential_exception
    
    username: str = payload.get("sub")
    if username is None:
        raise credential_exception
    
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credential_exception
    
    return user
                     