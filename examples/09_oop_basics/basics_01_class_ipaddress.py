class IPAddress:
    version = 4
    all_ip_set = set()

    def __init__(self, ip):
        print("__init__")
        self.ip = ip
        self.all_ip_set.add(ip)

    def pprint(self):
        print(f"IPAddress {self.ip}, Version {IPAddress.version}")
        print(f"IPAddress {self.ip}, Version {self.version}")
        print(f"IPAddress {self.ip}, Version {type(self).version}")


