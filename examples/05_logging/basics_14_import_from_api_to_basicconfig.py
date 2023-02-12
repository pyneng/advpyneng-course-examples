import logging

logging.basicConfig(
    level=logging.INFO,
    format="{name:20} {levelname:20} {lineno} {message}",
    style="{",
)

logging.debug("message debug")
logging.info("message info")
logging.warning("message warning")
