import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fmt = logging.Formatter("{asctime} {name} {levelname:10} {message}", style="{")

logfile = logging.FileHandler("log06.txt")
logfile.setLevel(logging.DEBUG)
logfile.setFormatter(fmt)

logger.addHandler(logfile)

## messages
logger.debug("Сообщение уровня debug")
logger.info("Сообщение уровня info")
logger.warning("Сообщение уровня warning")
