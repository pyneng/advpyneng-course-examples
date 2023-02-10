import logging
import paramiko
import netmiko
from netmiko import Netmiko, NetmikoTimeoutException
from rich.logging import RichHandler


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

fmt = logging.Formatter("{asctime} {name} {levelname:10} {message}", style="{")

# stderr
# stderr = logging.StreamHandler()
stderr = RichHandler(
    show_path=False,
    rich_tracebacks=True,
    tracebacks_extra_lines=5,
    tracebacks_show_locals=True,
    tracebacks_suppress=[netmiko, paramiko],
)
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)
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
    log.debug("After exception")


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
