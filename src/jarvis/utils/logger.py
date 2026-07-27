"""
Logging utilities.
"""

from __future__ import annotations

import logging
from pathlib import Path


def create_logger(log_directory: Path) -> logging.Logger:
    """
    Create the application logger.
    """

    log_directory.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("jarvis")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        log_directory / "jarvis.log",
        encoding="utf-8",
    )

    console_handler = logging.StreamHandler()

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger