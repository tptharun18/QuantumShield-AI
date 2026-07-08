from pathlib import Path
from loguru import logger
import sys

# Create logs directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Remove default logger
logger.remove()

# Console logging
logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan> - "
           "<level>{message}</level>",
)

# File logging
logger.add(
    LOG_DIR / "quantumshield.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="INFO",
)

# Error logging
logger.add(
    LOG_DIR / "errors.log",
    level="ERROR",
    rotation="5 MB",
    retention="60 days",
)

app_logger = logger