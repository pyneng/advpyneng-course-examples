import logging
from basics_13_code import func


logging.basicConfig(
    level=logging.INFO,
    format="{asctime} {levelname:10} {name} {module} {message}",
    style="{",
    force=True
)

logging.debug("message debug")
logging.info("message info")
logging.warning("message warning")
func()
