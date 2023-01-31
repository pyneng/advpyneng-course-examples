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
@click.argument("hosts", nargs=-1, required=True)
@click.option("-c", "--count", default=2, show_default=True, help="Кол-во ICMP запросов")
def cli(hosts, count):
    """
    Ping HOSTS
    """
    print(f"{hosts=} {count=}")
    for ip in hosts:
        status = ping_ip(ip, count)
        print(f"RESULTS {hosts=} {status=}")


if __name__ == "__main__":
    cli()
