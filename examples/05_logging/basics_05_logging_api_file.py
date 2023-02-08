import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logfile = logging.FileHandler("logfile.log")
logfile.setLevel(logging.WARNING)
formatter = logging.Formatter("{asctime} {name} {levelname} {message}", style="{")
logfile.setFormatter(formatter)

logger.addHandler(logfile)

## messages
logger.debug("Сообщение уровня debug")
logger.info("Сообщение уровня info")
logger.warning("Сообщение уровня warning")
