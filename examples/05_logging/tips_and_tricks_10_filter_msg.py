import logging
from rich import inspect


class MsgFilter(logging.Filter):
    def __init__(self, contains_text):
        self.contains_text = contains_text

    def filter(self, record):
        print(record)
        return self.contains_text in record.msg


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addFilter(MsgFilter("python"))

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(
    logging.Formatter(
        "{asctime} {name} {levelname:10} {message}", datefmt="%H:%M:%S", style="{"
    )
)
logger.addHandler(stderr)


for word in ["python", "ruby", "perl"]:
    logger.info(f"MSG {word}")
    logger.debug(f"MSG {word}")
