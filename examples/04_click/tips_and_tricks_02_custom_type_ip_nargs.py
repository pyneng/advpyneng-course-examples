import subprocess
import ipaddress
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


class IsIPv4(click.ParamType):
    def convert(self, value, param, ctx):
        print(f"{value=} {param=} {ctx=}")
        try:
            ip = ipaddress.ip_address(value)
            return str(ip)
        except ValueError:
            self.fail(f"'{value}' is not a valid IP address")


@click.command()
@click.argument("hosts", nargs=-1, required=True, type=IsIPv4())
@click.option("-c", "--count", default=2, show_default=True)
def cli(hosts, count):
    print(f"{hosts=} {count=}")
    for ip in hosts:
        status = ping_ip(ip, count)
        print(f"RESULTS {ip=} {status=}")


if __name__ == "__main__":
    cli()
