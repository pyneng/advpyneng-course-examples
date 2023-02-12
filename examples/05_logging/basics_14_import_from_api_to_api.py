import logging
from collections.abc import Iterable
from basics_14_code import func
from rich import inspect



log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

fmt = logging.Formatter(
    "{asctime} {name} {levelname:10} {message}", style="{"
)

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)

log.addHandler(stderr)


def remove_stream_handler(logger):
    for h in logger.handlers:
        if isinstance(h, logging.StreamHandler):
            logger.removeHandler(h)
    #if not logger.handlers:
        #logger.addHandler(logging.NullHandler())


def replace_handlers(logger, new_handlers):
    if not isinstance(new_handlers, Iterable):
        new_handlers = [new_handlers]
    for h_new in new_handlers:
        if not isinstance(h_new, logging.Handler):
            raise ValueError
    for h in logger.handlers:
        logger.removeHandler(h)
    for h_new in new_handlers:
        logger.addHandler(h_new)


log_14 = logging.getLogger("basics_14_code")
# replace_handlers(log_14, stderr)
inspect(log_14)
remove_stream_handler(log_14)
inspect(log_14)
# log_14 = logging.getLogger("basics_14_code")
# log_14.setLevel(logging.DEBUG)
# handlers = log_14.handlers
# for h in handlers:
#     log_14.removeHandler(h)
# log_14.addHandler(stderr)


log.debug("Сообщение уровня debug")
log.info("Сообщение уровня info")
log.warning("Сообщение уровня warning")
func()
