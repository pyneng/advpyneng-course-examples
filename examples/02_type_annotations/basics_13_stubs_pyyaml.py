from pprint import pprint
from typing import Union, TypedDict
import yaml


class NetmikoParams(TypedDict, total=False):
    device_type: str
    host: str
    username: str
    password: str
    secret: str
    timeout: int
    fast_cli: bool


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
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    pprint(send_show_command_to_devices(devices, "test"))
