import ipaddress
from collections.abc import Iterable
from typing import SupportsInt


class IPAddress:
    def __init__(self, ip: str, mask: int):
        self.ip = ip
        self.mask = mask

    def __int__(self) -> int:
        int_ip = int(ipaddress.ip_address(self.ip))
        return int_ip

    def __str__(self) -> str:
        return f"{self.ip}/{self.mask}"

    def __repr__(self) -> str:
        return f"IPAddress('{self.ip}', {self.mask})"


def convert_to_int(items: Iterable[SupportsInt]) -> list[int]:
    return [int(item) for item in items]


if __name__ == "__main__":
    ip1 = IPAddress("10.1.1.1", 25)
    ip2 = IPAddress("10.2.2.2", 25)
    ip3 = IPAddress("10.1.1.1", 25)
    print(convert_to_int([ip1, ip2, 10.5]))
