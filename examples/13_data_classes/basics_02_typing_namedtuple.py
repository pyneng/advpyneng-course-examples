from collections import namedtuple
from typing import NamedTuple


NetworkDevice = namedtuple("NetworkDevice", "hostname ip ios vendor")



class NetworkDevice(NamedTuple):
    hostname: str
    ip: str
    ios: str


r1 = NetworkDevice("r1", "10.1.1.1", "15.4")
r2 = NetworkDevice("r2", "10.2.2.2", "15.4")
r3 = NetworkDevice("r3", "10.3.3.3", "15.4")
r4 = NetworkDevice("r4", "10.4.4.4", "15.4")
r5 = NetworkDevice("r5", "10.5.5.5", "15.4")
