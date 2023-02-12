import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="{name} {levelname:10} {module:45} {message}",
    style="{",
    datefmt="%H:%M:%S"
)


def func():
    logging.debug("message debug")
    logging.info("message info")
    logging.warning("message warning")


if __name__ == "__main__":
    func()
