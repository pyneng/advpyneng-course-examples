from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
import time
import random

from netmiko import Netmiko
import click


def send_show_command(device, command):
    with Netmiko(**device) as ssh:
        ssh.enable()
        time.sleep(random.random() * 5)
        result = ssh.send_command(command)
    return result


def send_command_to_devices(devices, command, limit=1):
    results = {}
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [
            executor.submit(send_show_command, device, command) for device in devices
        ]
        with click.progressbar(devices, label="Подключение к устройствам:") as bar:
            for device, future in zip(bar, futures):
                results[device["host"]] = future.result()
    return results


@click.command()
@click.argument("command")
@click.argument("hosts", nargs=-1, required=True)
@click.option("-u", "--username", default="cisco")
@click.option("-p", "--password", default="cisco")
@click.option("-s", "--secret", default="cisco")
def cli(command, hosts, username, password, secret):
    device_params = {
        "device_type": "cisco_ios",
        "username": username,
        "password": password,
        "secret": secret,
    }

    device_list = [{**device_params, "host": ip} for ip in hosts]
    result = send_command_to_devices(device_list, command)
    pprint(result)


if __name__ == "__main__":
    cli()
