from pprint import pprint
from typing import Union


devices: list[dict[str, str | int | bool]] = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.100.2",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
        "timeout": 10,
        "fast_cli": False,
    },
]


# def send_show_command_to_devices(devices: list[dict[str, Union[str, int, bool]]], command)
def send_show_command_to_devices(
    devices: list[dict[str, str | int | bool]], command: str
) -> dict[str, str]:
    data = {}
    for device in devices:
        host = device["host"]
        output = f"{host}\n{command}"
        data[host] = output
    return data


def send_show_command_to_devices_1(
    devices: list[dict[str, str | int | bool]], command: str
) -> dict[str | bool | int, str]:
    data = {}
    for device in devices:
        host = device["host"]
        output = f"{host}\n{command}"
        data[host] = output
    return data


if __name__ == "__main__":
    pprint(send_show_command_to_devices(devices, "test"))
