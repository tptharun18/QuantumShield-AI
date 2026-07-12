from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.roles import require_role
from app.db.session import get_db
from app.models.user import User
from app.models.organization import Organization
from app.models.department import Department
from app.models.employee import Employee

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


# ==========================================================
# Enterprise Dashboard
# ==========================================================

@router.get("/stats")
def dashboard_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    organizations = db.query(Organization).count()

    departments = db.query(Department).count()

    employees = db.query(Employee).count()

    active_users = (
        db.query(User)
        .filter(User.is_active == True)
        .count()
    )

    inactive_users = (
        db.query(User)
        .filter(User.is_active == False)
        .count()
    )

    return {
        "organizations": organizations,
        "departments": departments,
        "employees": employees,
        "active_users": active_users,
        "inactive_users": inactive_users,
    }