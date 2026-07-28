"""
Simple intent analyzer.
"""

from .intent import Intent



class IntentAnalyzer:
    """
    Analyze user text.
    """


    def analyze(
        self,
        text: str,
    ) -> Intent:


        text = (
            text
            .lower()
            .strip()
        )


        # Remember pattern

        if (
            "my name is" in text
        ):

            name = (
                text
                .split(
                    "my name is"
                )[1]
                .strip()
            )


            return Intent(
                name="remember",
                entities={
                    "key": "name",
                    "value": name,
                },
            )


        # Recall pattern

        if (
            "what is my name" in text
            or
            "who am i" in text
        ):

            return Intent(
                name="recall",
                entities={
                    "key": "name"
                },
            )


        # Greeting

        if (
            text in [
                "hello",
                "hi",
                "hey",
            ]
        ):

            return Intent(
                name="hello",
                entities={},
            )


        return Intent(
            name="unknown",
            entities={},
        )