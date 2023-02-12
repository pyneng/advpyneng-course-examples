import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fmt = logging.Formatter("{asctime} {name} {levelname:10} {message}", style="{")

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)

logger.addHandler(stderr)


def func():
    logger.debug("Сообщение уровня debug")
    logger.info("Сообщение уровня info")
    logger.warning("Сообщение уровня warning")


if __name__ == "__main__":
    func()
