"""
Prompt builder.
"""

from .context import PromptContext



class PromptBuilder:
    """
    Build final LLM prompt.
    """



    def build(
        self,
        context: PromptContext,
    ) -> str:


        sections = []


        sections.append(
            "SYSTEM:\n"
            +
            context.system
        )


        if context.memory:

            memory_text = "\n".join(
                [
                    f"{k}: {v}"
                    for k, v
                    in context.memory.items()
                ]
            )


            sections.append(
                "MEMORY:\n"
                +
                memory_text
            )



        if context.history:

            history_text = "\n".join(
                context.history
            )


            sections.append(
                "HISTORY:\n"
                +
                history_text
            )



        sections.append(
            "USER:\n"
            +
            context.user_input
        )


        return "\n\n".join(
            sections
        )

