from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.models.department import Department
from app.models.employee import Employee

from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
)


# ==========================================================
# Get All Organizations
# ==========================================================

def get_all_organizations(db: Session):
    return db.query(Organization).all()


# ==========================================================
# Get Organization
# ==========================================================

def get_organization(
    db: Session,
    organization_id: int,
):
    return (
        db.query(Organization)
        .filter(Organization.id == organization_id)
        .first()
    )


# ==========================================================
# Create Organization
# ==========================================================

def create_organization(
    db: Session,
    organization: OrganizationCreate,
):
    db_org = Organization(**organization.model_dump())

    db.add(db_org)
    db.commit()
    db.refresh(db_org)

    return db_org


# ==========================================================
# Update Organization
# ==========================================================

def update_organization(
    db: Session,
    organization_id: int,
    organization: OrganizationUpdate,
):
    db_org = get_organization(
        db,
        organization_id,
    )

    if db_org is None:
        return None

    update_data = organization.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_org, key, value)

    db.commit()
    db.refresh(db_org)

    return db_org


# ==========================================================
# Delete Organization
# ==========================================================

def delete_organization(
    db: Session,
    organization_id: int,
):
    db_org = get_organization(
        db,
        organization_id,
    )

    if db_org is None:
        return None

    db.delete(db_org)
    db.commit()

    return {
        "message": "Organization deleted successfully"
    }


# ==========================================================
# Organization Statistics
# ==========================================================

def organization_stats(
    db: Session,
    organization_id: int,
):
    organization = get_organization(
        db,
        organization_id,
    )

    if organization is None:
        return None

    departments = (
        db.query(Department)
        .filter(
            Department.organization_id == organization_id
        )
        .count()
    )

    employees = (
        db.query(Employee)
        .join(
            Department,
            Employee.department_id == Department.id,
        )
        .filter(
            Department.organization_id == organization_id
        )
        .count()
    )

    return {
        "organization_id": organization.id,
        "organization_name": organization.name,
        "departments": departments,
        "employees": employees,
        "is_active": organization.is_active,
    }