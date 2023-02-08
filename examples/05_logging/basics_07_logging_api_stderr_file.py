import logging
from rich import inspect

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fmt = logging.Formatter("{asctime} {name} {levelname:10} {message}", style="{")

# file
logfile = logging.FileHandler("log07.txt")
logfile.setLevel(logging.INFO)
logfile.setFormatter(fmt)

logger.addHandler(logfile)

# stderr

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(
    logging.Formatter(
        "{asctime} {name} {levelname:10} {message}", style="{", datefmt="%H:%M:%S"
    )
)

logger.addHandler(stderr)

## messages
logger.debug("Сообщение уровня debug")
logger.info("Сообщение уровня info")
logger.warning("Сообщение уровня warning")
