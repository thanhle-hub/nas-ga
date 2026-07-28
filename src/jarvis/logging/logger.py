"""
JARVIS logging system.
"""

from __future__ import annotations

import logging
from pathlib import Path



class JarvisLogger:
    """
    Central logging manager.
    """


    def __init__(
        self,
        name: str = "jarvis",
        log_dir: str = "logs",
        level: int = logging.INFO,
    ) -> None:


        self.name = name

        self.log_dir = Path(
            log_dir
        )

        self.level = level


        self.logger = self._create()



    def _create(self) -> logging.Logger:
        """
        Create configured logger.
        """


        self.log_dir.mkdir(
            exist_ok=True
        )


        logger = logging.getLogger(
            self.name
        )


        logger.setLevel(
            self.level
        )


        # Remove old handlers
        # to support multiple instances/tests

        if logger.handlers:

            logger.handlers.clear()



        formatter = logging.Formatter(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        )



        console_handler = (
            logging.StreamHandler()
        )

        console_handler.setFormatter(
            formatter
        )



        file_handler = (
            logging.FileHandler(
                self.log_dir / "jarvis.log",
                encoding="utf-8",
            )
        )


        file_handler.setFormatter(
            formatter
        )



        logger.addHandler(
            console_handler
        )

        logger.addHandler(
            file_handler
        )


        return logger



    def get_logger(
        self,
    ) -> logging.Logger:
        """
        Return logger instance.
        """

        return self.logger