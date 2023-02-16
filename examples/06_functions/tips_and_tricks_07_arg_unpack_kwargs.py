

def config_interface(intf_name, ip_address, mask):
    interface = f"interface {intf_name}"
    no_shut = "no shutdown"
    ip_addr = f"ip address {ip_address} {mask}"
    result = [interface, no_shut, ip_addr]
    return result


# print(config_interface("Fa0/1", "10.0.1.1", "255.255.255.0"))
interfaces_info = [
    {"intf_name": "Fa0/1", "ip_address": "10.0.1.1", "mask": "255.255.255.0"},
    {"intf_name": "Fa0/2", "ip_address": "10.0.2.1", "mask": "255.255.255.0"},
    {"intf_name": "Fa0/3", "ip_address": "10.0.3.1", "mask": "255.255.255.0"},
    {"intf_name": "Fa0/4", "ip_address": "10.0.4.1", "mask": "255.255.255.0"},
]

intf1 = {"intf_name": "Fa0/1", "ip_address": "10.0.1.1", "mask": "255.255.255.0"}

print(config_interface(intf_name="Fa0/1", ip_address="10.0.1.1", mask="255.255.255.0"))
print(config_interface(**intf1))
