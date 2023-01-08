import ipaddress


def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def ping_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
