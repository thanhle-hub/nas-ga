"""
Event type definitions.
"""

from enum import Enum


class EventType(str, Enum):
    """
    System event names.
    """

    SYSTEM_START = "system.start"

    SYSTEM_STOP = "system.stop"

    COMMAND_RECEIVED = "command.received"

    AI_RESPONSE = "ai.response"

    PLUGIN_LOADED = "plugin.loaded"

    PLUGIN_STARTED = "plugin.started"

    PLUGIN_STOPPED = "plugin.stopped"

    ERROR_OCCURRED = "error.occurred"