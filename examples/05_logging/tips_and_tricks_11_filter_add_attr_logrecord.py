from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import logging
from pprint import pprint
import re

import yaml
from netmiko import (
    ConnectHandler,
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
)


class AddIPFilter(logging.Filter):
    def filter(self, record):
        match = re.search(r"\d+\.\d+\.\d+\.\d+", record.msg)
        if match:
            record.ip = match.group()
        else:
            record.ip = ""
        return True


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addFilter(AddIPFilter())

### stderr
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "{asctime} {name} {levelname:10} {ip:15} {message}", datefmt="%H:%M:%S", style="{"
)
console.setFormatter(formatter)
log.addHandler(console)


### File
logfile = logging.FileHandler("logfile3.log")
logfile.setLevel(logging.DEBUG)
formatter = logging.Formatter("{asctime} {name} {levelname} {message}", style="{")
logfile.setFormatter(formatter)

log.addHandler(logfile)


def send_show(device_dict, command):
    ip = device_dict["host"]
    log.info(f"===> Connection: {ip}")  #
    try:
        with ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            log.debug(f"<=== Received:   {ip}")
        return result
    except (NetMikoAuthenticationException, NetMikoTimeoutException) as err:
        log.warning(f"Ошибка при подключении {err}")


def send_command_to_devices(devices, command):
    log.debug(f"Подключаемся к {len(devices)} устройствам")
    data = {}
    with ThreadPoolExecutor(max_workers=3) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for device, output in zip(devices, result):
            data[device["host"]] = output
    return data


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    print(send_command_to_devices(devices, "sh clock"))
