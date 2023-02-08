import logging

from netmiko import Netmiko
from rich.logging import RichHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fmt = logging.Formatter(
    "{asctime} {name} {levelname:10} {message}", style="{"
)

# file
logfile = logging.FileHandler("logtt04.txt")
logfile.setLevel(logging.INFO)
logfile.setFormatter(fmt)

logger.addHandler(logfile)

# stderr

stderr = RichHandler(show_path=False)
stderr.setLevel(logging.INFO)
logger.addHandler(stderr)


def send_show_netmiko(device_dict, command):
    ip = device_dict["host"]
    logger.info(f"===> Connection: {ip}")

    with Netmiko(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
        logger.debug(f"<=== Received: output from {ip}\n{output}")
    return output


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
