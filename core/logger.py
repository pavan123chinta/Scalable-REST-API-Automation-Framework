import logging
import os


def setup_logger(name: str = "api_framework", level=logging.INFO):
    """
    Sets up and returns a configured logger.
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear existing handlers to avoid duplication
    if logger.handlers:
        logger.handlers.clear()

    # Create logs directory if not exists
    log_dir = "reports/logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "framework.log")

    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger