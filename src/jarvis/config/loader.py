"""
Configuration loader.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from .settings import JarvisSettings



class ConfigLoader:
    """
    Loads JARVIS configuration.
    """


    def __init__(
        self,
        path: str = "config/jarvis.yaml",
    ) -> None:

        self.path = Path(path)



    def load(self) -> JarvisSettings:
        """
        Read yaml configuration.
        """

        with self.path.open(
            "r",
            encoding="utf-8",
        ) as file:

            data = yaml.safe_load(file)


        return JarvisSettings(
            **data
        )