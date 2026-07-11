from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.auth.jwt import create_access_token
from app.auth.roles import require_role
from app.db.session import get_db
from app.models.user import User
from app.schemas.token import Token
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import (
    authenticate_user,
    create_user,
    get_user_by_email,
    get_user_by_username,
)

router = APIRouter()


# ==========================================================
# Register
# ==========================================================
@router.post("/register", response_model=UserResponse)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    if get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=400,
            detail="Username already exists",
        )

    if get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=400,
            detail="Email already exists",
        )

    return create_user(db, user)


# ==========================================================
# Login
# ==========================================================
@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(
        db,
        form_data.username,
        form_data.password,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    access_token = create_access_token(
        {
            "sub": user.username,
            "role": user.role,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


# ==========================================================
# Current Logged-in User
# ==========================================================
@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user


# ==========================================================
# Admin Dashboard
# ==========================================================
@router.get("/admin")
def admin_dashboard(
    current_user: User = Depends(require_role("Admin")),
):
    return {
        "message": "Welcome Admin",
        "user": current_user.username,
        "role": current_user.role,
    }


# ==========================================================
# Security Dashboard
# ==========================================================
@router.get("/analyst")
def analyst_dashboard(
    current_user: User = Depends(
        require_role(
            "Admin",
            "Security Analyst",
        )
    ),
):
    return {
        "message": "Security Dashboard",
        "user": current_user.username,
        "role": current_user.role,
    }


# ==========================================================
# Test Routes
# ==========================================================
@router.get("/")
def auth_home():
    return {
        "message": "Authentication Service Running"
    }


@router.get("/ping")
def ping():
    return {
        "status": "ok"
    }