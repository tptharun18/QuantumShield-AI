from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# ==========================
# Create Organization
# ==========================

class OrganizationCreate(BaseModel):
    name: str
    domain: str
    description: Optional[str] = None


# ==========================
# Update Organization
# ==========================

class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    domain: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


# ==========================
# Response
# ==========================

class OrganizationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    domain: str
    description: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime