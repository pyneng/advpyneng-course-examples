import subprocess
import ipaddress
from pprint import pprint
import click


def ping_ip(ip_address, count):
    """
    Ping ip_address and return True/False
    """
    print(f"Calling: ping -c {count} -n {ip_address} -W 1")
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


class ClickIPv4Address(click.ParamType):
    def convert(self, value, param, ctx):
        print(f"{value=} {param=} {ctx=}")
        try:
            ipaddress.ip_address(value)
            return value
        except ValueError:
            self.fail(f"'{value}' is not a valid IP address")


@click.command()
@click.argument("ipv4", type=ClickIPv4Address())
@click.option("-c", "--count", default=2, show_default=True)
def cli(ipv4, count):
    print(f"{ipv4=} {count=}")
    status = ping_ip(ipv4, count)
    print(f"RESULTS {ipv4=} {status=}")


if __name__ == "__main__":
    cli()

