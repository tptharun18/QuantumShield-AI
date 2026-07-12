from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String(200),
        unique=True,
        nullable=False,
        index=True,
    )

    domain = Column(
        String(200),
        unique=True,
        nullable=False,
        index=True,
    )

    description = Column(
        String(500),
        nullable=True,
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    departments = relationship(
        "Department",
        back_populates="organization",
        cascade="all, delete-orphan",
    )
    employees = relationship(
    "Employee",
    back_populates="organization",
    cascade="all, delete",
)