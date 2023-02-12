import logging

import yaml
from netmiko import Netmiko, NetmikoTimeoutException


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# stderr
stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(
    logging.Formatter("{asctime} {name} {levelname:10} {message}", style="{")
)
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
