import ipaddress


def check_ip(ip: str | int) -> bool:
    if type(ip) == int and 16777216 < ip < 3758096383:
        return True
    elif type(ip) == str:
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False
    else:
        raise ValueError


if __name__ == "__main__":
    print(check_ip("10.1.1.1"))
    print(check_ip("test"))
    print(check_ip(16777300))
    # print(check_ip(10.5))
