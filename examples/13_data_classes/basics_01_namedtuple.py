from collections import namedtuple


NetworkDevice = namedtuple("NetworkDevice", "hostname ios vendor ip")
r1 = NetworkDevice("r1", "15.4", "Cisco", "10.1.1.1")
