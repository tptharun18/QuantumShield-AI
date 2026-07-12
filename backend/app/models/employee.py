from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    employee_code = Column(
        String(30),
        unique=True,
        nullable=False,
    )

    first_name = Column(
        String(100),
        nullable=False,
    )

    last_name = Column(
        String(100),
        nullable=False,
    )

    email = Column(
        String(200),
        unique=True,
        nullable=False,
    )

    designation = Column(
        String(100),
        nullable=False,
    )

    phone = Column(
        String(20),
        nullable=True,
    )

    joining_date = Column(
        Date,
        nullable=True,
    )

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=True,
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # ======================================================
    # Relationships
    # ======================================================

    organization = relationship(
        "Organization",
        back_populates="employees",
    )

    department = relationship(
        "Department",
        back_populates="employees",
    )