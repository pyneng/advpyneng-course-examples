import logging
from rich import inspect


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fmt = logging.Formatter("{asctime} {name} {levelname:10} {message}", style="{")

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)

logger.addHandler(stderr)

def func():
    logger.debug("message debug")
    logger.info("message info")
    logger.warning("message warning")


if __name__ == "__main__":
    func()
