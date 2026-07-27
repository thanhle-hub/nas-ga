"""
JARVIS configuration models.
"""

from __future__ import annotations

from pydantic import BaseModel


class SystemSettings(BaseModel):

    name: str

    version: str



class PluginSettings(BaseModel):

    directory: str = "plugins"

    auto_load: bool = True



class AISettings(BaseModel):

    provider: str

    model: str



class VoiceSettings(BaseModel):

    enabled: bool = False



class LoggingSettings(BaseModel):

    level: str = "INFO"



class JarvisSettings(BaseModel):
    """
    Main application settings.
    """

    system: SystemSettings

    plugins: PluginSettings

    ai: AISettings

    voice: VoiceSettings

    logging: LoggingSettings