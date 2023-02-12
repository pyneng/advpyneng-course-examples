import logging

import yaml
import netmiko
import paramiko
from netmiko import Netmiko, NetmikoTimeoutException
from rich.logging import RichHandler


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# stderr
stderr = RichHandler(
    show_path=False,
    rich_tracebacks=True,
    tracebacks_suppress=[netmiko, paramiko],
    tracebacks_show_locals=True,
    tracebacks_extra_lines=5,
)
stderr.setLevel(logging.DEBUG)
log.addHandler(stderr)


def send_show_netmiko(device_dict, command):
    ip = device_dict["host"]
    log.info(f"===> Connection: {ip}")

    try:
        with Netmiko(**device_dict) as ssh:
            ssh.enable()
            output = ssh.send_command(command)
            log.debug(f"<=== Received: output from {ip}\n{output}")
        return output
    except NetmikoTimeoutException:
        log.exception("Возникла ошибка")


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        send_show_netmiko(dev, "sh ip int br")
