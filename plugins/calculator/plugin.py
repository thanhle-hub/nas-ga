from jarvis.plugins import Plugin


class CalculatorPlugin(Plugin):

    name = "calculator"

    version = "1.0.0"


    def activate(self) -> None:
        print(
            "Calculator plugin activated"
        )


    def deactivate(self) -> None:
        print(
            "Calculator plugin stopped"
        )