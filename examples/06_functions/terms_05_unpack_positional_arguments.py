from pprint import pprint


interfaces_info = [
    ["Fa0/1", "10.0.1.1", "255.255.255.0"],
    ["Fa0/2", "10.0.2.1", "255.255.255.0"],
    ["Fa0/3", "10.0.3.1", "255.255.255.0"],
    ["Fa0/4", "10.0.4.1", "255.255.255.0"],
    ["Lo0", "10.0.0.1", "255.255.255.255"],
]


def config_interface(intf_name, ip_address, mask):
    intf_cfg = [
        f"interface {intf_name}",
        "no shutdown",
        f"ip address {ip_address} {mask}",
    ]
    return intf_cfg


arg1 = ["Fa0/1", "10.0.1.1", "255.255.255.0"]
pprint(config_interface(*arg1))
pprint(config_interface("Fa0/1", "10.0.1.1", "255.255.255.0"))

for info in interfaces_info:
    pprint(config_interface(*info))
