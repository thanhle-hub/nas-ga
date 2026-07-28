"""
Autonomous agent loop.

Supports:
- Legacy ToolPipeline
- Reasoning + Decision architecture
"""

from __future__ import annotations


from .observer import Observer

from .evaluator import Evaluator

from .state import AgentState



class AgentLoop:
    """
    Agent execution loop.

    Flow:

    Observe
        |
    Reason
        |
    Decide
        |
    Act
        |
    Evaluate
    """



    def __init__(
        self,
        pipeline=None,
        reasoning=None,
        executor=None,
    ) -> None:


        self.pipeline = pipeline

        self.reasoning = reasoning

        self.executor = executor


        self.observer = Observer()

        self.evaluator = Evaluator()



    def _execute_pipeline(
        self,
        input_data: str,
    ):

        """
        Execute legacy tool pipeline.
        """


        if hasattr(
            self.pipeline,
            "run"
        ):

            return self.pipeline.run(
                input_data
            )


        if hasattr(
            self.pipeline,
            "execute"
        ):

            return self.pipeline.execute(
                input_data
            )


        if hasattr(
            self.pipeline,
            "handle"
        ):

            return self.pipeline.handle(
                input_data
            )


        if hasattr(
            self.pipeline,
            "process"
        ):

            return self.pipeline.process(
                input_data
            )


        if hasattr(
            self.pipeline,
            "invoke"
        ):

            return self.pipeline.invoke(
                input_data
            )


        if hasattr(
            self.pipeline,
            "call"
        ):

            return self.pipeline.call(
                input_data
            )


        raise AttributeError(
            "Unsupported tool pipeline interface"
        )



    def run(
        self,
        goal: str,
    ):


        #
        # Observe
        #
        observation = (
            self.observer
            .observe(
                goal
            )
        )



        #
        # Legacy Tool Pipeline Mode
        #
        if self.pipeline:


            result = (
                self._execute_pipeline(
                    observation.input
                )
            )


            return AgentState(

                finished=True,

                result=result,

                status="success",

                steps=[

                    "observe",

                    "execute",

                    "evaluate",

                ],

            )



        #
        # Autonomous Reasoning Mode
        #
        if self.reasoning is None:

            raise ValueError(
                "Reasoning engine is required"
            )



        #
        # Reason
        #
        thought = (
            self.reasoning
            .reason(
                observation.input
            )
        )



        #
        # Decide
        #
        decision = (
            self.reasoning
            .decide(
                observation.input
            )
        )



        #
        # Act
        #
        result = None


        if self.executor:


            result = (
                self.executor
                .execute(
                    decision.action
                )
            )



        #
        # Evaluate
        #
        status = (
            self.evaluator
            .evaluate(
                result
            )
        )



        return AgentState(

            finished=(
                status == "success"
            ),

            result={

                "thought": thought,

                "decision": decision,

                "result": result,

            },

            status=status,

            steps=[

                "observe",

                "reason",

                "decide",

                "act",

                "evaluate",

            ],

        )