"""
JARVIS Brain.
"""

from .analyzer import IntentAnalyzer



class Brain:
    """
    Main reasoning component.
    """


    def __init__(self):

        self.analyzer = IntentAnalyzer()



    def think(
        self,
        text: str,
    ):

        return self.analyzer.analyze(
            text
        )