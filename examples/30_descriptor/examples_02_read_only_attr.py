import logging
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    format="{msg}",
    style="{",
    handlers=[RichHandler(show_path=False)],
)


class LoggedAttrAccess:
    def __set_name__(self, owner, name):
        print(f"__set_name__ {owner=} {name=}")
        self.attr_name = "_" + name

    def __get__(self, instance, cls=None):
        print(f"__get__")
        value = getattr(instance, self.attr_name)
        logging.info(f"Read {self.attr_name}")
        return value

    def __set__(self, instance, value):
        print(f"__set__")
        logging.info(f"Write {self.attr_name} {value=}")
        raise AttributeError(f"can't set attribute '{self.attr_name}'")


class User:
    username = LoggedAttrAccess()
    password = LoggedAttrAccess()

    def __init__(self, username, password):
        self._username = username
        self._password = password

    def __repr__(self):
        return f"<{type(self).__name__} username={self.username}>"
