from dataclasses import dataclass, field
from ipaddress import ip_address


@dataclass(order=True)
class IPAddress:
    ip: str = field(compare=False)
    _ip_as_int: int = field(init=False, repr=False)
    mask: int

    def __post_init__(self):
        print("__post_init__")
        self._ip_as_int = int(ip_address(self.ip))
        if not isinstance(self.mask, int):
            raise TypeError("Маска должна быть числом")


ip1 = IPAddress("10.1.1.1", 24)
ip2 = IPAddress("10.10.1.2", 24)
ip3 = IPAddress("10.11.1.3", 24)
ip4 = IPAddress("10.20.1.4", 24)
ip5 = IPAddress("10.2.1.1", 24)

ip_list = [ip1, ip2, ip3, ip4, ip5]
