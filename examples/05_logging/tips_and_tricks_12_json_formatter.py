import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
formatter = jsonlogger.JsonFormatter(
    "{asctime} {name} {levelname} {message}", style="{"
)
stderr.setFormatter(formatter)
logger.addHandler(stderr)

for num in range(1, 31):
    logger.debug(f"MSG {num}")
