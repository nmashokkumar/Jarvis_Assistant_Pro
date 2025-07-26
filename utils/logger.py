# utils/logger.py

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Create logs directory if not exist
log_dir = Path(__file__).resolve().parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# Define log file path
log_file = log_dir / "app.log"

# Create rotating file handler
file_handler = RotatingFileHandler(
    log_file,
    maxBytes=5 * 1024 * 1024,  # 5 MB
    backupCount=5,
    encoding="utf-8"
)

# Create console handler with warning level to avoid spamming
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# Define formatter
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Apply formatter
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Initialize root logger only once
root_logger = logging.getLogger()
if not root_logger.handlers:
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

def get_logger(name="JarvisLogger"):
    """
    Returns a logger with the given name, ready to use anywhere.
    Usage:
        from utils.logger import get_logger
        logger = get_logger(__name__)
        logger.info("message")
    """
    return logging.getLogger(name)

# Self-test
if __name__ == "__main__":
    logger = get_logger("LoggerTest")
    logger.info("Logger initialized successfully.")
    logger.warning("Logger warning test.")
    logger.error("Logger error test.")
