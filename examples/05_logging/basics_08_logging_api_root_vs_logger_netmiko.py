import logging
from netmiko import Netmiko

logging.getLogger("netmiko").setLevel(logging.WARNING)
logging.getLogger("paramiko").setLevel(logging.INFO)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

fmt = logging.Formatter(
    "{asctime} {name} {levelname:10} {message}", style="{"
)

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)

log.addHandler(stderr)

log.debug("Сообщение уровня debug")
log.info("Сообщение уровня info")
log.warning("Сообщение уровня warning")

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
