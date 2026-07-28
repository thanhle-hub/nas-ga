"""
JARVIS CLI.
"""

from jarvis.brain import BrainPipeline



class CLIInterface:

    def __init__(
        self,
        pipeline: BrainPipeline,
    ):

        self.pipeline = pipeline

        self.running = True



    def start(self):

        print("=" * 40)

        print(
            "       JARVIS READY"
        )

        print("=" * 40)


        while self.running:


            try:

                text = input(
                    "\nYou: "
                )


                if text.lower() == "exit":

                    print(
                        "JARVIS: Shutting down..."
                    )

                    break



                response = (
                    self.pipeline.process(
                        text
                    )
                )


                print(
                    "JARVIS:",
                    response
                )


            except KeyboardInterrupt:

                break