from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.roles import require_role
from app.db.session import get_db
from app.models.user import User

from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentResponse,
)

from app.services.department_service import (
    create_department,
    get_all_departments,
    get_department,
    update_department,
    delete_department,
)

router = APIRouter(
    prefix="/departments",
    tags=["Departments"],
)


@router.post("/", response_model=DepartmentResponse)
def create(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    return create_department(db, department)


@router.get("/", response_model=list[DepartmentResponse])
def get_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    return get_all_departments(db)


@router.get("/{department_id}", response_model=DepartmentResponse)
def get_one(
    department_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    department = get_department(db, department_id)

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found",
        )

    return department


@router.put("/{department_id}", response_model=DepartmentResponse)
def update(
    department_id: int,
    payload: DepartmentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    department = update_department(
        db,
        department_id,
        payload,
    )

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found",
        )

    return department


@router.delete("/{department_id}")
def delete(
    department_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    result = delete_department(
        db,
        department_id,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found",
        )

    return result