devices = [
    {
        "hostname": "london_r1",
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    {
        "hostname": "london_r2",
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    {
        "hostname": "london_sw1",
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
    },
]


device_list = [
    ("r21", "Manchester", "Cisco", "15.4", "10.252.0.1"),
    ("sw21", "Coventry", "Cisco", "3.6.XE", "10.253.0.3"),
    ("sw21", "Manchester", "Cisco", "3.6.XE", "10.252.0.3"),
    ("london_r1", "London", "Cisco", "15.4", "10.255.0.1"),
    ("r21", "Manchester", "Cisco", "15.4", "10.252.0.2"),
    ("london_sw1", "London", "Cisco", "3.6.XE", "10.255.0.3"),
    ("r21", "Coventry", "Cisco", "15.4", "10.253.0.1"),
    ("london_r2", "London", "Cisco", "15.4", "10.255.0.2"),
    ("r21", "Coventry", "Cisco", "15.4", "10.253.0.2"),
]


vlans = [("IT_VLAN", 320), ("Mngmt_VLAN", 99), ("User_VLAN", 1010), ("DB_VLAN", 11)]

words = ["one", "two", "list", "instance", "dict", "TEST", "DICT"]
