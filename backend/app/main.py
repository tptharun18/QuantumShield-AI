from fastapi import FastAPI
from app.core.settings import settings
from app.core.logger import app_logger
from app.db.postgres import check_postgres

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app_logger.info("QuantumShield AI started successfully")


@app.get("/")
def root():
    app_logger.info("Root endpoint accessed")
    return {
        "message": f"Welcome to {settings.APP_NAME}"
    }


@app.get("/health")
def health():
    app_logger.info("Health endpoint accessed")
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG
    }

@app.get("/database")
def database_status():

    if check_postgres():
        return {
            "status": "connected",
            "database": "quantumshield"
        }

    return {
        "status": "disconnected"
    }