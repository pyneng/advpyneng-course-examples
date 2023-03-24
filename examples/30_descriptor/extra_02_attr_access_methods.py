import logging
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    format="{msg}",
    style="{",
    handlers=[RichHandler(show_path=False)],
)


class LogAttrAccess:
    def __getattribute__(self, name):
        logging.info(f"__getattribute__ {name=}")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        logging.info(f"__setattr__ {name=}, {value=}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        logging.info(f"__delattr__ {name=}")
        super().__delattr__(name)

    def __getattr__(self, name):
        logging.info(f"__getattr__ {name=}")
        raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{name}'")
