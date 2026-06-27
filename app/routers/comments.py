from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, models
from app.dependencies import get_db, get_current_user

router = APIRouter(prefix="/posts/{post_id}/comments", tags=["Comments"])

@router.post("/", response_model=schemas.CommentOut)
def create_comment(
    post_id: int,
    comment: schemas.CommentCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    post = crud.get_post(db, post_id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="Post not found")
    
    return crud.create_comment(db, comment, author_id=current_user.id, post_id=post_id)

@router.get("/", response_model=List[schemas.CommentOut])
def read_comments(post_id: int, db: Session = Depends(get_db)):
    return crud.get_comments_for_post(db, post_id)


@router.delete("/{comment_id}")
def delete_comment(
    post_id: int,
    comment: id,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()

    if comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    
    if comment.author_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this comment")
    
    crud.delete_comment(db, comment_id)
    return {"detail": "Commentr deleted successfully"}

