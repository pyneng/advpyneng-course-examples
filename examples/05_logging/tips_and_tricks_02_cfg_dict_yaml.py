from pprint import pprint
import logging
import logging.config
import yaml

# create logger
logger = logging.getLogger(__name__)

# read config
with open("config_log.yml") as f:
    log_config = yaml.safe_load(f)

logging.config.dictConfig(log_config)

## messages
logger.debug("Сообщение уровня debug")
logger.info("Сообщение уровня info")
logger.warning("Сообщение уровня warning")
