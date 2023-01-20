import ipaddress


class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    def __int__(self):
        int_ip = int(ipaddress.ip_address(self.ip))
        return int_ip

    def __str__(self):
        return f"{self.ip}/{self.mask}"

    def __repr__(self):
        return f"IPAddress('{self.ip}', {self.mask})"

    def __lt__(self, second_ip):
        if type(second_ip) != IPAddress:
            raise TypeError(f"'<' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (int(self), self.mask) < (int(second_ip), second_ip.mask)

    def __le__(self, second_ip):
        if type(second_ip) != IPAddress:
            raise TypeError(f"'<=' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (int(self), self.mask) <= (int(second_ip), second_ip.mask)

    def __eq__(self, second_ip):
        if type(second_ip) != IPAddress:
            raise TypeError(f"'==' not supported between instances of 'IPAddress'"
                            f" and '{type(second_ip).__name__}'")
        return (int(self), self.mask) == (int(second_ip), second_ip.mask)


if __name__ == "__main__":
    ip1 = IPAddress("10.1.1.1", 25)
    ip2 = IPAddress("10.2.2.2", 25)
    ip3 = IPAddress("10.1.1.1", 25)
    ip4 = IPAddress("10.10.1.1", 25)
    ip5 = IPAddress("10.1.1.1", 29)

