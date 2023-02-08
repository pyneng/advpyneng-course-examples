import logging

root = logging.getLogger()
root.setLevel(logging.DEBUG)

fmt = logging.Formatter(
    "{asctime} {name} {levelname:10} {message}", style="{"
)

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)

root.addHandler(stderr)

root.debug("Сообщение уровня debug")
root.info("Сообщение уровня info")
root.warning("Сообщение уровня warning")

# root messages
# logging.debug("LOGGING Сообщение уровня debug")
# logging.info("LOGGING Сообщение уровня info")
# logging.warning("LOGGING Сообщение уровня warning")
