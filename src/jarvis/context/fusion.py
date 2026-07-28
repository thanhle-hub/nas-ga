"""
Context fusion layer.
"""

from .context import AgentContext



class ContextFusion:
    """
    Combine memory and knowledge.
    """



    def combine(
        self,
        memories: list[str],
        knowledge: list[str],
    ) -> AgentContext:


        return AgentContext(

            memories=memories,

            knowledge=knowledge,

        )