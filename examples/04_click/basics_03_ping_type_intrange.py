import subprocess
from pprint import pprint
import click


def ping_ip(ip_address, count):
    """
    Ping IP_ADDRESS and return True/False
    """
    reply = subprocess.run(
        f"ping -c {count} -n {ip_address} -W 1",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    if reply.returncode == 0:
        return True
    else:
        return False


@click.command()
@click.argument("host")
@click.option(
    "-c", "--count", default=2, show_default=True, type=click.IntRange(1, 10, clamp=True)
)
def cli(host, count):
    """
    Ping HOST
    """
    print(f"{host=} {count=}")
    status = ping_ip(host, count)
    print(f"RESULTS {host=} {status=}")


if __name__ == "__main__":
    cli()
