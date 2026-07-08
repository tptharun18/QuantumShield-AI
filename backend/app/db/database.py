from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from app.core.settings import settings

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)

engine = create_engine(
    DATABASE_URL,
    echo=settings.DEBUG,
    future=True
)

Base = declarative_base()