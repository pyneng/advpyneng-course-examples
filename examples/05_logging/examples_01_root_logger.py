import logging
from pprint import pprint
from scrapli import Scrapli
from netmiko import Netmiko


logging.basicConfig(
    format="{asctime} {name:20} {levelname:8} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.INFO,
)


def send_show_scrapli(device, show_command):
    ip = device["host"]
    logging.info(f"===> Connection: {ip}")
    with Scrapli(**device) as ssh:
        reply = ssh.send_command(show_command)
        output = reply.result
    logging.info(f"<=== Received:   {ip}")
    return output


def send_show_netmiko(device_dict, command):
    ip = device_dict["host"]
    logging.info(f"===> Connection: {ip}")

    with Netmiko(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        logging.info(f"<=== Received:   {ip}")
    return result


if __name__ == "__main__":
    r1s = {
        "host": "192.168.100.1",
        "auth_username": "cisco",
        "auth_password": "cisco",
        "auth_secondary": "cisco",
        "auth_strict_key": False,
        "timeout_socket": 5,
        "timeout_transport": 10,
        "platform": "cisco_iosxe",
    }
    r2n = {
        "host": "192.168.100.2",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
        "device_type": "cisco_ios",
        "timeout": 5,
    }

    send_show_scrapli(r1s, "sh ip int br")
    send_show_netmiko(r2n, "sh ip int br")
