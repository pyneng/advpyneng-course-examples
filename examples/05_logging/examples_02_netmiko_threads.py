from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import logging
from itertools import repeat

import yaml
from netmiko import Netmiko, NetmikoBaseException
from paramiko.ssh_exception import SSHException


logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("netmiko").setLevel(logging.WARNING)

logging.basicConfig(
    format="{threadName} {asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.DEBUG,
)


def send_show(device_dict, command):
    host = device_dict["host"]
    logging.info(f">>> Подключаюсь к {host}")
    try:
        with Netmiko(**device_dict) as conn:
            conn.enable()
            logging.debug(f"Отправляю команду {command} на {host}")
            output = conn.send_command(command)
            logging.info(f"<<< Получили вывод {host}")
            return output
    except (NetmikoBaseException, SSHException) as error:
        logging.error(f"Возникла ошибка на {host} {error}")


def send_show_to_devices(device_list, command, threads=5):
    host_output_dict = {}
    with ThreadPoolExecutor(max_workers=threads) as ex:
        all_results = ex.map(send_show, device_list, repeat(command))
        for device, out in zip(device_list, all_results):
            host = device["host"]
            host_output_dict[host] = out
    return host_output_dict


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    data = send_show_to_devices(devices, "sh clock")
    pprint(data)

