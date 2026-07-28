from jarvis.bootstrap import JarvisBootstrap

from jarvis.brain import (
    Brain,
    BrainExecutor,
    BrainPipeline,
)

from jarvis.interface import CLIInterface

from jarvis.memory import MemoryManager



def main():

    bootstrap = JarvisBootstrap()

    bootstrap.start()


    memory = MemoryManager()


    brain = Brain()


    executor = BrainExecutor(
        memory
    )


    pipeline = BrainPipeline(
        brain,
        executor,
    )


    cli = CLIInterface(
        pipeline
    )


    cli.start()



if __name__ == "__main__":

    main()