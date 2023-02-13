import logging
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logfile = TimedRotatingFileHandler(
    "logfile_with_timedrotation.log", when="S", interval=5, backupCount=3
    # "logfile_with_timedrotation.log", when="H", interval=10, backupCount=3
    # "logfile_with_timedrotation.log", when="D", interval=1, backupCount=3
)
logfile.setLevel(logging.DEBUG)
logfile.setFormatter(
    logging.Formatter(
        "{asctime} {name} {levelname} {message}", datefmt="%H:%M:%S", style="{"
    )
)
logger.addHandler(logfile)

for num in range(1, 31):
    logger.debug(f"MSG {num}")
    time.sleep(1)
