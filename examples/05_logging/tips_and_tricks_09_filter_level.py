import logging
from rich import inspect


class DebugOnlyFilter(logging.Filter):
    def filter(self, record):
        # inspect(record)
        return record.levelname == "DEBUG"


class LevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addFilter(LevelFilter(logging.INFO))
# logger.addFilter(DebugOnlyFilter())

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(
    logging.Formatter(
        "{asctime} {name} {levelname:10} {message}", datefmt="%H:%M:%S", style="{"
    )
)
# stderr.addFilter(DebugOnlyFilter())
logger.addHandler(stderr)

### File
logfile = logging.FileHandler("logfile09.log")
logfile.setLevel(logging.DEBUG)
formatter = logging.Formatter("{asctime} {name} {levelname} {message}", style="{")
logfile.setFormatter(formatter)
logger.addHandler(logfile)


for num in range(1, 11):
    logger.info(f"MSG {num}")
    logger.debug(f"MSG {num}")
