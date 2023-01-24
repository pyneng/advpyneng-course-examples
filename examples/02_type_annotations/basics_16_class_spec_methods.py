import ipaddress
from typing import Any


class IPAddress:
    def __init__(self, ip: str, mask: int):
        self.ip = ip
        self.mask = mask

    def __int__(self) -> int:
        int_ip = int(ipaddress.ip_address(self.ip))
        return int_ip

    def _int_to_str(self, ip_as_int: int) -> str:
        return str(ipaddress.ip_address(ip_as_int))

    def __str__(self) -> str:
        return f"{self.ip}/{self.mask}"

    def __repr__(self) -> str:
        return f"IPAddress('{self.ip}', {self.mask})"

    def __add__(self, other: int) -> IPAddress:
        if type(other) != int:
            raise TypeError(f"'+' not supported between instances of 'IPAddress'"
                            f" and '{type(other).__name__}'")
        new_ip = self._int_to_str(int(self) + other)
        return IPAddress(new_ip, self.mask)

    def __eq__(self, second_ip: object) -> bool:
        if type(second_ip) != IPAddress:
            raise TypeError(f"'==' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (int(self), self.mask) == (int(second_ip), second_ip.mask)

    def __lt__(self, second_ip: IPAddress) -> bool:
        if type(second_ip) != IPAddress:
            raise TypeError(f"'<' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (int(self), self.mask) < (int(second_ip), second_ip.mask)


if __name__ == "__main__":
    ip1 = IPAddress("10.1.1.1", 25)
    ip2 = IPAddress("10.2.2.2", 25)
    ip3 = IPAddress("10.1.1.1", 25)
    ip4 = IPAddress("10.10.1.1", 25)
    ip5 = IPAddress("10.1.1.1", 29)


