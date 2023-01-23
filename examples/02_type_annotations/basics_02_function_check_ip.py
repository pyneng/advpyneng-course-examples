import ipaddress


def check_ip(ip: str | int) -> bool:
    if type(ip) == str and ip in range(16777216, 4026531840):
        return True
    elif type(ip) == str:
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError as err:
            return False
    else:
        raise ValueError


if __name__ == "__main__":
    print(check_ip("10.1.1.1"))
    print(check_ip("test"))
    print(check_ip(100))

