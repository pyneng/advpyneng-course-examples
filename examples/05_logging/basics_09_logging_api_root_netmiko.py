import logging
from netmiko import Netmiko


log = logging.getLogger()
log.setLevel(logging.DEBUG)
# netmiko/paramiko
logging.getLogger("netmiko").setLevel(logging.DEBUG)
logging.getLogger("paramiko").setLevel(logging.INFO)

fmt = logging.Formatter("{asctime} {name} {levelname:10} {message}", style="{")

# stderr
stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)

log.addHandler(stderr)

# file
logfile = logging.FileHandler("log09.txt")
logfile.setLevel(logging.DEBUG)
logfile.setFormatter(fmt)

log.addHandler(logfile)


def send_show_netmiko(device_dict, command):
    ip = device_dict["host"]
    log.info(f"===> Connection: {ip}")

    with Netmiko(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
        log.debug(f"<=== Received: output from {ip}\n{output}")
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
