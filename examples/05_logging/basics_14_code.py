import logging
from rich import inspect

logging.basicConfig()

logger = logging.getLogger("test")
#logger.setLevel(logging.DEBUG)
#logger.addHandler(logging.NullHandler())

fmt = logging.Formatter("{asctime} {name:10} {levelname:10} {message}", style="{")

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)

logger.addHandler(stderr)
logger.propagate = False
print(f"{logger.getEffectiveLevel()=}")


new = logging.getLogger("test.new")
new.warning("message warning")

def func():
    logger.debug("message debug")
    logger.info("message info")
    logger.warning("message warning")


if __name__ == "__main__":
    func()
