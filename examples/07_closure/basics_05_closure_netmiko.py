from netmiko import Netmiko

r1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}


def netmiko_ssh(**params_dict):
    conn = Netmiko(**params_dict)
    conn.enable()

    def inner(command):
        return conn.send_command(command)
    return inner

