# Placeholder for utils/logger.py

# utils/logger.py

import logging
from pathlib import Path

# Create logs directory if it doesn't exist
log_dir = Path(__file__).resolve().parent.parent / "logs"
log_dir.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=log_dir / "app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# Function to get logger in modules
def get_logger(name="JarvisLogger"):
    return logging.getLogger(name)


# Example usage
if __name__ == "__main__":
    logger = get_logger()
    logger.info("Logger initialized successfully.")
    logger.warning("This is a test warning.")
    logger.error("This is a test error.")
