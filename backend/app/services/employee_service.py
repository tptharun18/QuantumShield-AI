from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
)


# ==========================================================
# Create Employee
# ==========================================================

def create_employee(
    db: Session,
    employee: EmployeeCreate,
):
    db_employee = Employee(**employee.model_dump())

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


# ==========================================================
# Get All Employees
# ==========================================================

def get_all_employees(db: Session):
    return db.query(Employee).all()


# ==========================================================
# Get Employee
# ==========================================================

def get_employee(
    db: Session,
    employee_id: int,
):
    return (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )


# ==========================================================
# Update Employee
# ==========================================================

def update_employee(
    db: Session,
    employee_id: int,
    payload: EmployeeUpdate,
):
    employee = get_employee(db, employee_id)

    if employee is None:
        return None

    update_data = payload.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(employee, key, value)

    db.commit()
    db.refresh(employee)

    return employee


# ==========================================================
# Delete Employee
# ==========================================================

def delete_employee(
    db: Session,
    employee_id: int,
):
    employee = get_employee(db, employee_id)

    if employee is None:
        return None

    db.delete(employee)
    db.commit()

    return {
        "message": "Employee deleted successfully"
    }
# ==========================================================
# Search Employee by Name
# ==========================================================

def search_employee_by_name(
    db: Session,
    name: str,
):
    return (
        db.query(Employee)
        .filter(
            Employee.first_name.ilike(f"%{name}%")
        )
        .all()
    )


# ==========================================================
# Search Employee by Email
# ==========================================================

def search_employee_by_email(
    db: Session,
    email: str,
):
    return (
        db.query(Employee)
        .filter(
            Employee.email.ilike(f"%{email}%")
        )
        .all()
    )


# ==========================================================
# Employees by Department
# ==========================================================

def employees_by_department(
    db: Session,
    department_id: int,
):
    return (
        db.query(Employee)
        .filter(
            Employee.department_id == department_id
        )
        .all()
    )