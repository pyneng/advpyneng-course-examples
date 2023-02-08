import logging

# root logger
# logger = logging.getLogger()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fmt = logging.Formatter(
    "{asctime} {name} {levelname:10} {message}", style="{"
)

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)

logger.addHandler(stderr)

logger.debug("Сообщение уровня debug")
logger.info("Сообщение уровня info")
logger.warning("Сообщение уровня warning")

# root messages
logging.debug("LOGGING Сообщение уровня debug")
logging.info("LOGGING Сообщение уровня info")
logging.warning("LOGGING Сообщение уровня warning")
