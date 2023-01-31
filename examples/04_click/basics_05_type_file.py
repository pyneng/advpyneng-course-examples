from pprint import pprint
import yaml
import click


def send_show_command(device, command):
    pass


def send_command_to_devices(devices, command, limit=10):
    pass


@click.command()
@click.argument("command")
@click.option("-y", "--yaml-params", type=click.File("r"), default="devices.yaml")
@click.option("-o", "--output", type=click.File("w"))
def cli(yaml_params, command, output):
    """
    Отправить команду COMMAND на устройства из файла DEVICES-PARAMS
    """
    print(f"{yaml_params=}")
    print(f"{output=}")
    devices = yaml.safe_load(yaml_params)
    output.write(command)
    print(f"{output=}")


if __name__ == "__main__":
    cli()
