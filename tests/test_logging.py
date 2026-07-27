from pathlib import Path

from jarvis.logging import JarvisLogger



def test_logger_creation(
    tmp_path: Path,
):

    logger_system = JarvisLogger(
        log_dir=str(tmp_path)
    )


    logger = logger_system.get_logger()


    logger.info(
        "JARVIS test message"
    )


    log_file = (
        tmp_path /
        "jarvis.log"
    )


    assert log_file.exists()


    content = log_file.read_text(
        encoding="utf-8"
    )


    assert (
        "JARVIS test message"
        in content
    )