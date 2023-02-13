import logging
from collections.abc import Iterable
from rich import inspect
from basics_14_code import func
# from basics_14_code_file import func

def replace_handlers(logger, new_handlers):
    if not isinstance(new_handlers, Iterable):
        new_handlers = [new_handlers]
    for h in logger.handlers:
        logger.removeHandler(h)
    for new_h in new_handlers:
        logger.addHandler(new_h)


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(
    logging.Formatter("{asctime} {name:20} {levelname:10} {message}", style="{")
)
log.addHandler(stderr)
# inspect(log)

l14 = logging.getLogger("basics_14_code")
replace_handlers(l14, stderr)


func()
log.debug("Сообщение уровня debug")
log.info("Сообщение уровня info")
log.warning("Сообщение уровня warning")
