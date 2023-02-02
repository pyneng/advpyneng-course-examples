from pprint import pprint
import click
from rich import inspect

def send_command_to_devices(devices, command, limit=10):
    return f"OUTPUT: {command}\n{devices}"


@click.command()
@click.argument("command")
@click.argument("hosts", nargs=-1, required=True)
@click.option("-u", "--username", prompt=True)
@click.option("-p", "--password", envvar="NETMIKO_PASSWORD", prompt=True, hide_input=True)
@click.option("-s", "--secret", prompt=True, hide_input=True)
@click.pass_context
def cli(ctx, command, hosts, username, password, secret):
    print(f"{ctx=} {command=} {hosts=} {username=} {password=} {secret=}")
    # inspect(ctx, methods=True)
    for param in ctx.params:
        print(f"{param:10}{ctx.get_parameter_source(param)=}")
    # pprint(ctx.get_help())
    device_params = {
        "device_type": "cisco_ios",
        "username": username,
        "password": password,
        "secret": secret,
    }

    device_list = [{**device_params, "host": ip} for ip in hosts]
    result = send_command_to_devices(device_list, command)


if __name__ == "__main__":
    cli()
