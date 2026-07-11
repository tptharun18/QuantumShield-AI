from sqlalchemy.orm import Session

from app.models.user import User


def get_all_users(db: Session):
    return db.query(User).all()


def update_role(
    db: Session,
    user_id: int,
    role: str,
):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return None

    user.role = role

    db.commit()
    db.refresh(user)

    return user


def update_status(
    db: Session,
    user_id: int,
    is_active: bool,
):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return None

    user.is_active = is_active

    db.commit()
    db.refresh(user)

    return user


def delete_user(
    db: Session,
    user_id: int,
):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return None

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }