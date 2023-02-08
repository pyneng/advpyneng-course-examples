import logging
from basics_11_nullhandler_code import send_show_netmiko

logging.basicConfig(
    level=logging.INFO,
    format="{asctime} {levelname:10} {name} {message}",
    style="{",
    datefmt="%H:%M:%S"
)

logging.info("TEST")

if __name__ == "__main__":
    r1 = {
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
        "device_type": "cisco_ios",
        "timeout": 5,
    }

    send_show_netmiko(r1, "sh ip int br")

