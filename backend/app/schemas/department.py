from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# ==========================================================
# Create Department
# ==========================================================

class DepartmentCreate(BaseModel):
    name: str
    description: Optional[str] = None
    organization_id: int


# ==========================================================
# Update Department
# ==========================================================

class DepartmentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


# ==========================================================
# Response
# ==========================================================

class DepartmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: Optional[str]
    organization_id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime