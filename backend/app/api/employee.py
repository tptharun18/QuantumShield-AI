from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.roles import require_role
from app.db.session import get_db
from app.models.user import User

from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse,
)

from app.services.employee_service import (
    create_employee,
    get_all_employees,
    get_employee,
    update_employee,
    delete_employee,
    search_employee_by_name,
    search_employee_by_email,
    employees_by_department,
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)


# ==========================================================
# Create Employee
# ==========================================================

@router.post(
    "/",
    response_model=EmployeeResponse,
)
def create(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    return create_employee(
        db,
        employee,
    )


# ==========================================================
# Get All Employees
# ==========================================================

@router.get(
    "/",
    response_model=list[EmployeeResponse],
)
def get_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    return get_all_employees(db)


# ==========================================================
# Get Employee
# ==========================================================

@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
def get_one(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    employee = get_employee(
        db,
        employee_id,
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found",
        )

    return employee


# ==========================================================
# Update Employee
# ==========================================================

@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
def update(
    employee_id: int,
    payload: EmployeeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    employee = update_employee(
        db,
        employee_id,
        payload,
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found",
        )

    return employee


# ==========================================================
# Delete Employee
# ==========================================================

@router.delete("/{employee_id}")
def delete(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    employee = delete_employee(
        db,
        employee_id,
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found",
        )
    # ==========================================================
# Search by Name
# ==========================================================

@router.get("/search/name/{name}")
def search_name(
    name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    return search_employee_by_name(
        db,
        name,
    )


# ==========================================================
# Search by Email
# ==========================================================

@router.get("/search/email/{email}")
def search_email(
    email: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    return search_employee_by_email(
        db,
        email,
    )


# ==========================================================
# Employees by Department
# ==========================================================

@router.get("/department/{department_id}")
def by_department(
    department_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    return employees_by_department(
        db,
        department_id,
    )

    return employee