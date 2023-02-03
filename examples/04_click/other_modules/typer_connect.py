import typer
from netmiko import Netmiko
import yaml


def send_show_command(device, command):
    with Netmiko(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_command_to_cisco_devices(device_list, command):
    result = {}
    for device in device_list:
        ip = device["host"]
        result[ip] = send_show_command(device, command)
    return result


def main(
    command: str,
    ip_list: list[str],
    username: str = typer.Option(..., prompt=True),
    password: str = typer.Option(
        ..., "--password", "-p", envvar="NET_PASSWORD", prompt=True, hide_input=True
    ),
    secret: str = typer.Option(..., "-s", prompt=True, hide_input=True),
):
    device_params = {
        "device_type": "cisco_ios",
        "username": username,
        "password": password,
        "secret": secret,
    }

    device_list = [{**device_params, "host": ip} for ip in ip_list]

    result_dict = send_command_to_cisco_devices(device_list, command)
    for ip, output in result_dict.items():
        print(ip.center(30, "="))
        print(output)


if __name__ == "__main__":
    typer.run(main)
