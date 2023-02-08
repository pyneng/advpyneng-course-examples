from pprint import pprint
import logging
import logging.config
from rich import inspect

# create logger
logger = logging.getLogger(__name__)
# inspect(logger)

cfg = {
    "version": 1,
    "formatters": {
        "file_fmt": {"format": "{asctime} {name} {levelname} {message}", "style": "{"},
        "stderr_fmt": {
            "format": "{asctime} {name} {levelname} {message}",
            "style": "{",
            "datefmt": "%H:%M:%S",
        },
    },
    "handlers": {
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "stderr_fmt",
            "stream": "ext://sys.stderr",
        },
        "logfile": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "file_fmt",
            "filename": "logfile.txt",
        },
    },
    "loggers": {
        "__main__": {
            "level": "DEBUG",
            "handlers": ["stderr", "logfile"],
        }
    },
}

logging.config.dictConfig(cfg)
# inspect(logger)

## messages
logger.debug("Сообщение уровня debug")
logger.info("Сообщение уровня info")
logger.warning("Сообщение уровня warning")
