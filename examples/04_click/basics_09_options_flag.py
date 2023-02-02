from pprint import pprint
import logging
import click


logging.basicConfig(
    format="{asctime} {name} {levelname} {message}",
    datefmt="%H:%M:%S",
    style="{",
    level=logging.INFO,
)


def send_command_to_devices(devices, command, limit=10):
    logging.info(f"Connecting to devices...")
    for dev in devices:
        logging.debug(f"Send command {command} to device {dev['host']}")
    return f"OUTPUT: {command}\n{devices}"


@click.command()
@click.argument("command")
@click.argument("hosts", nargs=-1, required=True)
@click.option("-u", "--username", default="cisco")
@click.option("-p", "--password", default="cisco")
@click.option("-s", "--secret", default="cisco")
@click.option("-d", "--debug", is_flag=True)
def cli(command, hosts, username, password, secret, debug):
    print(f"{command=} {debug=}")
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
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
