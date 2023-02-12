import logging
from collections.abc import Iterable
from basics_14_code import func



log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

fmt = logging.Formatter(
    "{asctime} {name} {levelname:10} {message}", style="{"
)

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)

log.addHandler(stderr)


def replace_handlers(logger, new_handlers):
    if not isinstance(new_handlers, Iterable):
        new_handlers = [new_handlers]
    handlers = logger.handlers
    for h in handlers:
        logger.removeHandler(h)
    for h_new in new_handlers:
        logger.addHandler(h_new)


log_14 = logging.getLogger("basics_14_code")
replace_handlers(log_14, stderr)
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
