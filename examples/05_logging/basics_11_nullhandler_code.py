import logging
from netmiko import Netmiko


log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def send_show_netmiko(device_dict, command):
    ip = device_dict["host"]
    log.info(f"===> Connection: {ip}")

    with Netmiko(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
        log.debug(f"<=== Received: output from {ip}\n{output}")
    return output

