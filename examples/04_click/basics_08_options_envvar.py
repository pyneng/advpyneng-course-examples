from pprint import pprint
import click


def send_command_to_devices(devices, command, limit=10):
    return f"OUTPUT: {command}\n{devices}"


@click.command()
@click.argument("command")
@click.argument("hosts", nargs=-1, required=True)
@click.option("-u", "--username", envvar="NET_USER", prompt=True)
@click.option("-p", "--password", prompt=True, hide_input=True)
@click.option("-s", "--secret", prompt=True, hide_input=True)
def cli(command, hosts, username, password, secret):
    print(f"{command=} {hosts=} {username=} {password=} {secret=}")
    device_params = {
        "device_type": "cisco_ios",
        "username": username,
        "password": password,
        "secret": secret,
    }

    device_list = [{**device_params, "host": ip} for ip in hosts]
    result = send_command_to_devices(device_list, command)


if __name__ == "__main__":
    cli(auto_envvar_prefix="NETMIKO")
