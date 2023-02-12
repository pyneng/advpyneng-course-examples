import logging
from rich import inspect

logger = logging.getLogger("test")

# logger.setLevel(logging.DEBUG)
#
# fmt = logging.Formatter(
#     "{asctime} {name:10} {levelname:10} {message}", style="{", datefmt="%H:%M:%S"
# )
#
# stderr = logging.StreamHandler()
# stderr.setLevel(logging.DEBUG)
# stderr.setFormatter(fmt)
# logger.addHandler(stderr)
#
# new = logging.getLogger("test.new")
# new.propagate = False
#
# new.warning("NEW msg")

# inspect(new)

def func():
    logger.debug("message debug")
    logger.info("message info")
    logger.warning("message warning")


if __name__ == "__main__":
    func()
