from functools import total_ordering
from collections import namedtuple

IP = namedtuple("IPAddress", "ip mask")
ip1 = IP("10.1.1.1", 25)
print(ip1)


@total_ordering
class IPAddress:
    slots = ()
    def __init__(self, ip, mask):
        self._ip = ip
        self._mask = mask

    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mask

    def __repr__(self):
        return f"IPAddress(ip='{self.ip}', mask={self.mask})"

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.ip, self.mask) < (other.ip, other.mask)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.ip, self.mask) == (other.ip, other.mask)

ip1 = IPAddress("10.1.1.1", 25)
print(ip1.ip)
