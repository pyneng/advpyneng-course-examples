import subprocess
import ipaddress
from pprint import pprint
import click


def ping_ip(ip_address, count):
    """
    Ping IP_ADDRESS and return True/False
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
        # if isinstance(value, ipaddress.IPv4Address):
        #    return value
        try:
            ip = ipaddress.ip_address(value)
            return ip
        except ValueError:
            self.fail(f"'{value}' is not a valid IP address")


@click.command()
@click.argument("hosts", type=ClickIPv4Address(), nargs=-1, required=True)
@click.option("-c", "--count", default=2, show_default=True)
def cli(hosts, count):
    print(f"{hosts=} {count=}")
    for ip in hosts:
        status = ping_ip(ip, count)
        print(f"RESULTS {ip=} {status=}")


if __name__ == "__main__":
    cli()

