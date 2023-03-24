import logging
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    format="{msg}",
    style="{",
    handlers=[RichHandler(show_path=False)],
)


class LoggedAttrAccess:
    def __init__(self, attr_name):
        print(f"__init__ {attr_name}")
        self.attr_name = attr_name

    def __get__(self, instance, cls=None):
        print(f"__get__")
        value = getattr(instance, self.attr_name)
        logging.info(f"Read {self.attr_name}")
        return value

    def __set__(self, instance, value):
        print(f"__set__")
        logging.info(f"Write {self.attr_name} {value=}")
        setattr(instance, self.attr_name, value)


class User:
    username = LoggedAttrAccess("_username")
    password = LoggedAttrAccess("_password")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<{type(self).__name__} username={self.username}>"
