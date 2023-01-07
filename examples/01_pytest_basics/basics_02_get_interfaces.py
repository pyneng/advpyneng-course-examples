from pprint import pprint
import re


def get_interfaces_from_cfg(config_str):
    match_all = re.finditer(r"^interface (\S+)", config_str, re.MULTILINE)
    interfaces = [m.group(1) for m in match_all]
    return interfaces


def get_intf_ip_from_cfg(config_str):
    regex = re.compile(
        r"interface (?P<intf>\S+)\n"
        r"( .*\n)*"
        r" ip address (?P<ip>\S+) (?P<mask>\S+)"
    )
    match_all = regex.finditer(config_str)

    result = {m.group("intf"): m.group("ip", "mask") for m in match_all}
    return result


if __name__ == "__main__":
    with open("config_r1.txt") as f1:
        cfg1 = f1.read()
    with open("config_r2.txt") as f2:
        cfg2 = f2.read()

    pprint(get_interfaces_from_cfg(cfg1))
    pprint(get_interfaces_from_cfg(cfg2))
    pprint(get_intf_ip_from_cfg(cfg1))
    pprint(get_intf_ip_from_cfg(cfg2))
