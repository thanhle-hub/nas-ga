from dataclasses import dataclass


@dataclass
class LLMResponse:

    text: str

    model: str = ""

    usage: dict | None = None


    def __str__(self):

        return self.text


    def __contains__(
        self,
        item,
    ):

        return item in self.text


    def __eq__(
        self,
        other,
    ):

        if isinstance(
            other,
            str,
        ):

            return self.text == other

        return super().__eq__(other)