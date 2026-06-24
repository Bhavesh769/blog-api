from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import hash_password


#--------------User Crud-----------------

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


#-------------Post CRUD---------------


def get_post(db:Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts(db:Session, skip: int = 0, limit: int = 10):
    return db.query(models.Post).offset(skip).limit(limit).all()

def create_post(db:Session, post: schemas.PostCreate, author_id: int):
    db_post = models.Post(
        title=post.title,
        content=post.content,
        author_id=author_id
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db:Session, post_id: int):
    db_post = get_post(db, post_id)
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post



#--------------Comment CRUD---------------


def get_comments_for_post(db:Session, post_id: int):
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).all()

def create_comment(db: Session, comment: schemas.CommentCreate, author_id: int, post_id: int):
    db_comment = models.Comment(
        content = comment.content
        author_id=author_id
        post_id=post_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
    return db_comment







