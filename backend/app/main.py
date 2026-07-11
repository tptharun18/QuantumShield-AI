from fastapi import FastAPI

from app.core.settings import settings
from app.core.logger import app_logger
from app.db.postgres import check_postgres

# Routers
from app.auth.router import router as auth_router
from app.api.admin import router as admin_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# ==========================================================
# Register Routers
# ==========================================================

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"],
)

app.include_router(admin_router)

app_logger.info("QuantumShield AI started successfully")


# ==========================================================
# Root
# ==========================================================

@app.get("/")
def root():
    app_logger.info("Root endpoint accessed")
    return {
        "message": f"Welcome to {settings.APP_NAME}"
    }


# ==========================================================
# Health Check
# ==========================================================

@app.get("/health")
def health():
    app_logger.info("Health endpoint accessed")
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG
    }


# ==========================================================
# Database Status
# ==========================================================

@app.get("/database")
def database_status():
    if check_postgres():
        return {
            "status": "connected",
            "database": settings.POSTGRES_DB
        }

    return {
        "status": "disconnected"
    }