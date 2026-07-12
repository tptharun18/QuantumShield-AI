from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate,
)


def create_department(
    db: Session,
    department: DepartmentCreate,
):
    new_department = Department(
        name=department.name,
        description=department.description,
        organization_id=department.organization_id,
    )

    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return new_department


def get_all_departments(db: Session):
    return db.query(Department).all()


def get_department(
    db: Session,
    department_id: int,
):
    return (
        db.query(Department)
        .filter(Department.id == department_id)
        .first()
    )


def update_department(
    db: Session,
    department_id: int,
    payload: DepartmentUpdate,
):
    department = (
        db.query(Department)
        .filter(Department.id == department_id)
        .first()
    )

    if department is None:
        return None

    update_data = payload.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(department, key, value)

    db.commit()
    db.refresh(department)

    return department


def delete_department(
    db: Session,
    department_id: int,
):
    department = (
        db.query(Department)
        .filter(Department.id == department_id)
        .first()
    )

    if department is None:
        return None

    db.delete(department)
    db.commit()

    return {
        "message": "Department deleted successfully"
    }