import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:10} {name} {module} {funcName} {lineno} {message}",
    style="{",
    datefmt="%H:%M:%S"
)

logging.debug("message debug")
logging.info("message info")
logging.warning("message warning")


def func():
    logging.debug("message debug")
    logging.info("message info")
    logging.warning("message warning")


func()
