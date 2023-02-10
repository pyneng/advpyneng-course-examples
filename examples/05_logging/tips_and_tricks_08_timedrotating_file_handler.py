import logging
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logfile = TimedRotatingFileHandler(
    "logfile_with_rotation.log", when=10, backupCount=3
)
logfile.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "{asctime} {name} {levelname} {message}", datefmt="%H:%M:%S", style="{"
)
logfile.setFormatter(formatter)

logger.addHandler(logfile)

## messages
logger.debug("Сообщение уровня debug")
time.sleep(2)
logger.info("Сообщение уровня info")
time.sleep(2)
logger.warning("Сообщение уровня warning")
