from jarvis.context import (
    ContextFusion,
)



def test_context_fusion():


    fusion = ContextFusion()


    context = fusion.combine(

        memories=[
            "User uses STM32"
        ],

        knowledge=[
            "STM32 uses ARM Cortex-M"
        ]

    )


    assert (
        "User uses STM32"
        in context.memories
    )


    assert (
        "STM32 uses ARM Cortex-M"
        in context.knowledge
    )