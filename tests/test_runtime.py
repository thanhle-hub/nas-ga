import logging

from jarvis.core import Runtime


def test_runtime_start_stop() -> None:
    logger = logging.getLogger("test")

    runtime = Runtime(logger)

    assert runtime.is_running is False

    runtime.start()

    assert runtime.is_running is True

    runtime.stop()

    assert runtime.is_running is False