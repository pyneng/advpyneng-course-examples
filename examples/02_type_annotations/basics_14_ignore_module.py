from pprint import pprint
import ipaddress
from advpyneng_cli_course.utils import green, red # type: ignore


def check_ip(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        print(green(ip))
        return True
    except ValueError as err:
        print(red(ip))
        return False


if __name__ == "__main__":
    print(check_ip("10.1.1.1"))
    print(check_ip("test"))
