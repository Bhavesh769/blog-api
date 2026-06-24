from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

#--------------------------------User Schemas---------------------------------#

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True



#-------------------------------Post Schemas---------------------------------#

class PostCreate(BaseModel):
    title: str
    content: str

class PostOut(BaseModel):
    id: int 
    title: str
    content: str
    author_id: int
    created_at: datetime

    class Config:
        from_attributes = True


    
#------------------------------------Comment Schemas-------------------------------------


class CommentCreate(BaseModel):
    content: str

class CommentOut(BaseModel):
    id: int
    content: str
    author_id: int
    post_id: int
    created_at: datetime

    class Config:
        from_attributes = True


