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
@click.argument("ipv4")
@click.option("-c", "--count", default=2, show_default=True)
def cli(ipv4, count):
    print(f"{ipv4=} {count=}")
    status = ping_ip(ipv4, count)
    print(f"RESULTS {ipv4=} {status=}")

if __name__ == "__main__":
    cli()
