from pprint import pprint
from typing import Union, TypedDict


class NetmikoParams(TypedDict, total=False):
    device_type: str
    host: str
    username: str
    password: str
    secret: str
    timeout: int
    fast_cli: bool


devices: list[NetmikoParams] = [
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


def send_show_command_to_devices(
    devices: list[NetmikoParams], command: str
) -> dict[str, str]:
    data = {}
    for device in devices:
        host = device["host"]
        output = f"{host}\n{command}"
        data[host] = output
    return data


if __name__ == "__main__":
    pprint(send_show_command_to_devices(devices, "test"))
