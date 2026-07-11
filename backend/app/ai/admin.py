from fastapi import APIRouter, Depends

from app.auth.roles import require_role
from app.models.user import User

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get("/dashboard")
def dashboard(
    current_user: User = Depends(require_role("Admin")),
):
    return {
        "message": "QuantumShield Admin Dashboard",
        "user": current_user.username,
        "role": current_user.role,
    }


@router.get("/users")
def list_users(
    current_user: User = Depends(require_role("Admin")),
):
    return {
        "message": "Only Admins can view users"
    }