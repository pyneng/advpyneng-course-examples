import logging
from logging.handlers import RotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logfile = RotatingFileHandler("logfile_with_rotation.log", maxBytes=100, backupCount=3)
logfile.setLevel(logging.DEBUG)
logfile.setFormatter(
    logging.Formatter(
        "{asctime} {name} {levelname} {message}", datefmt="%H:%M:%S", style="{"
    )
)
logger.addHandler(logfile)

## messages
for num in range(1, 21):
    logger.debug(f"MSG {num}")
    time.sleep(1)
