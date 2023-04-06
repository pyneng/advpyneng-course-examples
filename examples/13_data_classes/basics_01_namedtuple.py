from collections import namedtuple


NetworkDevice = namedtuple("NetworkDevice", "hostname ip ios vendor")

r1 = NetworkDevice("r1", "10.1.1.1", "15.4", "Cisco")
r2 = NetworkDevice("r2", "10.2.2.2", "15.4", "Cisco")
r3 = NetworkDevice("r3", "10.3.3.3", "15.4", "Cisco")
r4 = NetworkDevice("r4", "10.4.4.4", "15.4", "Cisco")
r5 = NetworkDevice("r5", "10.5.5.5", "15.4", "Cisco")
