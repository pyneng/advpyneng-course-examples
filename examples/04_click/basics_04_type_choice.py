from pprint import pprint
import click


@click.command()
@click.argument("host", type=click.Choice(["8.8.8.8", "192.168.100.1", "10.1.1.1"]))
def cli(host):
    print(f"{host=}")


if __name__ == "__main__":
    cli()
