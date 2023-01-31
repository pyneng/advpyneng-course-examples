from pprint import pprint
import yaml
import click


def send_command_to_devices(devices, command, limit=10):
    return f"OUTPUT: {command}\n{devices}"


@click.command()
@click.argument("command")
@click.option(
    "-y",
    "--yaml-params",
    type=click.Path(exists=True, dir_okay=False, resolve_path=True),
)
@click.option("-o", "--output", type=click.Path(dir_okay=False))
def cli(yaml_params, command, output):
    """
    Отправить команду COMMAND на устройства из файла DEVICES-PARAMS
    """
    print(f"{yaml_params=}")
    print(f"{output=}")
    with open(yaml_params) as f:
        devices = yaml.safe_load(f)

    result = send_command_to_devices(devices, command)
    with open(output, "w") as dst:
        dst.write(result)


if __name__ == "__main__":
    cli()
