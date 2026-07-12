from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


# ==========================================================
# Base
# ==========================================================

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    designation: str
    employee_code: str
    department_id: int


# ==========================================================
# Create
# ==========================================================

class EmployeeCreate(EmployeeBase):
    pass


# ==========================================================
# Update
# ==========================================================

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    designation: Optional[str] = None
    department_id: Optional[int] = None
    is_active: Optional[bool] = None


# ==========================================================
# Response
# ==========================================================

class EmployeeResponse(EmployeeBase):
    id: int
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }