from pprint import pprint
from typing import Union, TypeAlias


ListDictStrStr = list[dict[str, str]]
# Python >= 3.10
# ListDictStrStr: TypeAlias = list[dict[str, str]]

devices: ListDictStrStr = [
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
    },
]


def send_show_command_to_devices(
    devices: ListDictStrStr, command: str
) -> dict[str, str]:
    data = {}
    for device in devices:
        host = device["host"]
        output = f"{host}\n{command}"
        data[host] = output
    return data


if __name__ == "__main__":
    pprint(send_show_command_to_devices(devices, "test"))
