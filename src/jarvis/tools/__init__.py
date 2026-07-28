"""
JARVIS Tool System.
"""

from .descriptor import ToolDescriptor
from .registry import ToolRegistry
from .selector import ToolSelector
from .executor import ToolExecutor
from .caller import ToolCaller
from .result import ToolResult



# Chỉ import nếu các file này đã tồn tại
try:
    from .executor import ToolExecutor
except ImportError:
    ToolExecutor = None

try:
    from .tool import Tool
except ImportError:
    Tool = None

try:
    from .manager import ToolManager
except ImportError:
    ToolManager = None


__all__ = [
    "ToolDescriptor",
    "ToolRegistry",
]

if ToolExecutor is not None:
    __all__.append("ToolExecutor")

if Tool is not None:
    __all__.append("Tool")

if ToolManager is not None:
    __all__.append("ToolManager")