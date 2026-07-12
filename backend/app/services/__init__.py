"""
QuantumShield AI Services Package
"""

# ==========================================================
# User Services
# ==========================================================

from .user_service import (
    create_user,
    authenticate_user,
    get_user_by_username,
    get_user_by_email,
)

# ==========================================================
# Admin Services
# ==========================================================

from .admin_service import (
    get_all_users,
    update_role,
    update_status,
    delete_user,
)

# ==========================================================
# Organization Services
# ==========================================================

from .organization_service import (
    create_organization,
    get_all_organizations,
    get_organization,
    update_organization,
    delete_organization,
)

# ==========================================================
# Department Services
# ==========================================================

from .department_service import (
    create_department,
    get_all_departments,
    get_department,
    update_department,
    delete_department,
)

# ==========================================================
# Employee Services
# ==========================================================

from .employee_service import (
    create_employee,
    get_all_employees,
    get_employee,
    update_employee,
    delete_employee,
)

# ==========================================================
# Exports
# ==========================================================

__all__ = [
    # User
    "create_user",
    "authenticate_user",
    "get_user_by_username",
    "get_user_by_email",

    # Admin
    "get_all_users",
    "update_role",
    "update_status",
    "delete_user",

    # Organization
    "create_organization",
    "get_all_organizations",
    "get_organization",
    "update_organization",
    "delete_organization",

    # Department
    "create_department",
    "get_all_departments",
    "get_department",
    "update_department",
    "delete_department",

    # Employee
    "create_employee",
    "get_all_employees",
    "get_employee",
    "update_employee",
    "delete_employee",
]