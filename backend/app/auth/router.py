from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import (
    create_user,
    get_user_by_email,
    get_user_by_username,
)

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):

    if get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")

    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already exists")

    return create_user(db, user)


@router.get("/")
def auth_home():
    return {"message": "Authentication Service Running"}


@router.get("/ping")
def ping():
    return {"status": "ok"}