from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.roles import require_role
from app.db.session import get_db
from app.models.user import User

from app.schemas.admin import (
    UpdateUserRole,
    UpdateUserStatus,
)

from app.services.admin_service import (
    get_all_users,
    update_role,
    update_status,
    delete_user,
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)