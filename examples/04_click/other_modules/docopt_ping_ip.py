"""
Ping IP_ADDRESS

Usage:
  example_01_ping_function.py -c <count> IP_ADDRESS

Options:
  -c, --count INTEGER  Number of packets
  --help               Show this message and exit.
"""
from docopt import docopt
import subprocess


def ping_ip(ip_address, count):
    """
    Ping IP address and return True/False
    """
    reply = subprocess.run(
        f"ping -c {count} -n {ip_address}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    if reply.returncode == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    args = docopt(__doc__)
    # print(args)
    reply = ping_ip(args.get("IP_ADDRESS"), args.get("--count"))
    if reply:
        print(f"IP address {ip_address} is reachable")
    else:
        print(f"IP address {ip_address} is unreachable")


