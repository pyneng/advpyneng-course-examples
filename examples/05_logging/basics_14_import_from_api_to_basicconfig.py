import logging
from basics_14_code import func


logging.basicConfig(
    # filename="log14.txt",
    level=logging.INFO,
    format="{name:20} {levelname:10} {lineno} {message}",
    style="{",
)

func()
logging.debug("message debug")
logging.info("message info")
logging.warning("message warning")
