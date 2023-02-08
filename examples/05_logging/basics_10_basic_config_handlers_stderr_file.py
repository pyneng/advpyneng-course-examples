import logging

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)

logfile = logging.FileHandler("log10.txt")
logfile.setLevel(logging.DEBUG)

logging.basicConfig(
    handlers=[stderr, logfile],
    level=logging.DEBUG,
    format="{asctime} {levelname:10} {name} {message}",
    style="{",
)


## messages
logging.debug("Сообщение уровня debug")
logging.info("Сообщение уровня info")
logging.warning("Сообщение уровня warning")
