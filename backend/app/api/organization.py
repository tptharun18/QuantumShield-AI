from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.roles import require_role
from app.db.session import get_db
from app.models.user import User

from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
    OrganizationResponse,
)

from app.services.organization_service import (
    create_organization,
    get_all_organizations,
    get_organization,
    update_organization,
    delete_organization,
    organization_stats,
)

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)


# ==========================================================
# Create Organization
# ==========================================================

@router.post(
    "/",
    response_model=OrganizationResponse,
)
def create(
    organization: OrganizationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    return create_organization(db, organization)


# ==========================================================
# Get All Organizations
# ==========================================================

@router.get(
    "/",
    response_model=list[OrganizationResponse],
)
def get_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    return get_all_organizations(db)


# ==========================================================
# Get Organization
# ==========================================================

@router.get(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def get_one(
    organization_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    organization = get_organization(
        db,
        organization_id,
    )

    if organization is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found",
        )

    return organization


# ==========================================================
# Update Organization
# ==========================================================

@router.put(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def update(
    organization_id: int,
    payload: OrganizationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    organization = update_organization(
        db,
        organization_id,
        payload,
    )

    if organization is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found",
        )

    return organization


# ==========================================================
# Delete Organization
# ==========================================================

@router.delete("/{organization_id}")
def delete(
    organization_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    organization = delete_organization(
        db,
        organization_id,
    )

    if organization is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found",
        )

    return {
        "message": "Organization deleted successfully"
    }


# ==========================================================
# Organization Statistics
# ==========================================================

@router.get("/{organization_id}/stats")
def stats(
    organization_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("Admin")),
):
    data = organization_stats(
        db,
        organization_id,
    )

    if data is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found",
        )

    return data