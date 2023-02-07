import logging

logging.basicConfig(
    filename="log02.txt",
    level=logging.DEBUG,
    format="{asctime} {levelname:10} {name} {module} {funcName} {lineno} {message}",
    style="{",
)

logging.debug("message debug")
logging.info("message info")
logging.warning("message warning")


def func():
    logging.debug("message debug")
    logging.info("message info")
    logging.warning("message warning")


func()
