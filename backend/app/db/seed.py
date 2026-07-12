from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.auth.hashing import get_password_hash

from app.models.user import User
from app.models.organization import Organization
from app.models.department import Department
from app.models.employee import Employee


def seed():

    db: Session = SessionLocal()

    try:

        # =====================================================
        # Admin User
        # =====================================================

        if not db.query(User).filter(User.username == "admin").first():

            admin = User(
                username="admin",
                email="admin@quantumshield.ai",
                full_name="System Administrator",
                hashed_password=get_password_hash("Admin@123"),
                role="Admin",
                is_active=True,
            )

            db.add(admin)

        # =====================================================
        # Organization
        # =====================================================

        org = db.query(Organization).first()

        if org is None:

            org = Organization(
                name="QuantumShield AI",
                domain="quantumshield.ai",
                description="Enterprise Cybersecurity Platform",
                is_active=True,
            )

            db.add(org)
            db.commit()
            db.refresh(org)

        # =====================================================
        # Department
        # =====================================================

        dept = db.query(Department).first()

        if dept is None:

            dept = Department(
                name="Cyber Security",
                description="Security Operations Center",
                organization_id=org.id,
                is_active=True,
            )

            db.add(dept)
            db.commit()
            db.refresh(dept)

        # =====================================================
        # Employees
        # =====================================================

        if db.query(Employee).count() == 0:

            employees = [

                Employee(
                    first_name="Alice",
                    last_name="Johnson",
                    email="alice@quantumshield.ai",
                    phone="9876543210",
                    designation="Security Analyst",
                    employee_code="EMP001",
                    department_id=dept.id,
                    is_active=True,
                ),

                Employee(
                    first_name="Bob",
                    last_name="Smith",
                    email="bob@quantumshield.ai",
                    phone="9876543211",
                    designation="SOC Engineer",
                    employee_code="EMP002",
                    department_id=dept.id,
                    is_active=True,
                ),

            ]

            db.add_all(employees)

        db.commit()

        print("Database seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed()