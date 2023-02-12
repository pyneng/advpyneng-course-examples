import logging
from pprint import pprint
from netmiko import Netmiko
from rich import inspect


logging.getLogger("netmiko").propagate = False
# logging.getLogger("paramiko.transport").propagate = False

p = logging.getLogger("paramiko")
p.setLevel(logging.DEBUG)
p.propagate = False

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(
    logging.Formatter(
        "{asctime} {name} {levelname:10} {message}",
        style="{",
        datefmt="%H:%M:%S",
    )
)
p.addHandler(stderr)


logging.basicConfig(
    format="{asctime} {name:20} {levelname:8} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)


def send_show_netmiko(device_dict, command):
    ip = device_dict["host"]
    logging.info(f"===> Connection: {ip}")

    with Netmiko(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        logging.info(f"<=== Received:   {ip}")
    return result


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
