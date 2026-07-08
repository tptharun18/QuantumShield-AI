from sqlalchemy import text

from app.db.database import engine


def check_postgres():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception:
        return False