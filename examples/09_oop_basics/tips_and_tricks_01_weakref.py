from weakref import WeakSet


class IPAddress:
    version = 4
    all_ip_set = WeakSet()

    def __init__(self, ip):
        print("__init__")
        self.ip = ip
        self.all_ip_set.add(self)

    def pprint(self):
        print(f"IPAddress {self.ip}, Version {type(self).version}")


