import logging
from rich import inspect

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(
    logging.Formatter("{name:20} {levelname:10} {message}", style="{")
)
logger.addHandler(stderr)


def func():
    logger.debug("MSG1")
    logger.info("MSG2")
    logger.warning("MSG3")


if __name__ == "__main__":
    func()
