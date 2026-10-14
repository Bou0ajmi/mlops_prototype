

import logging
import sys
from src.exception import CustomException


def get_logger(name: str = "main", level: int = logging.INFO) -> logging.Logger:
    """Return a logger that prints to the terminal."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding duplicate handlers if get_logger is called more than once
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

    return logger


if __name__ == "__main__":
    # Simple test: simulate a tiny training loop
    log = get_logger("test_logger", level=logging.DEBUG)

    log.debug("Debug message: loading config")
    log.info("Starting training")
    log.warning("Validation loss did not improve")
    log.error("Example error message yes there is a problem")

    log.info("Training finished")

    try:
        y=5/0
    except Exception as e:
        log.error(CustomException(e, sys))
