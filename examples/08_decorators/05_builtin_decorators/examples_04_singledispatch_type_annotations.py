from netmiko import Netmiko
import yaml
from pprint import pprint
from collections.abc import Sequence
from functools import singledispatch


@singledispatch
def send_commands(command, device):
    raise ValueError(f"Тип {type(command).__name__} не поддерживается")


@send_commands.register
def _(show_command: str, device):
    print("show")
    with Netmiko(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show_command)
    return result


@send_commands.register
def _(config_commands: Sequence[str], device):
    print("config")
    with Netmiko(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
    return result


if __name__ == "__main__":
    commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
    show_command = "sh ip int br"
    with open("devices.yaml") as f:
        dev_list = yaml.safe_load(f)
        r1 = dev_list[0]

    pprint(send_commands(tuple(commands), r1))
    pprint(send_commands(show_command, r1), width=120)
