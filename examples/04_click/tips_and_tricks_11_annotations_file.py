from pprint import pprint
from typing import IO
import yaml
import click


def send_command_to_devices(
    devices: list[dict[str, str]], command: str, limit: int = 10
) -> str:
    return f"OUTPUT: {command}\n{devices}"


@click.command()
@click.argument("command")
@click.option("-y", "--yaml-params", type=click.File("r"))
@click.option("-o", "--output", type=click.File("w"))
def cli(yaml_params: IO[str], command: str, output: IO[str]) -> None:
    """
    Отправить команду COMMAND на устройства из файла DEVICES-PARAMS
    """
    print(f"{yaml_params=}")
    print(f"{output=}")
    devices = yaml.safe_load(yaml_params)

    result = send_command_to_devices(devices, command)
    output.write(result)
    print(f"{output=}")


if __name__ == "__main__":
    cli()
