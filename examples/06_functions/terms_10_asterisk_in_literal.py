# New in Python 3.5
# PEP 448 – Additional Unpacking Generalizations https://peps.python.org/pep-0448/
from pprint import pprint

# list/tuple/set and *

cmd_list = ["interface Gi0/1", "switchport mode access", "switchport access vlan 10"]
all_cmd_list = ["conf t", *cmd_list, "end"]
pprint(all_cmd_list)


cmd_list1 = ["interface Gi0/1", "switchport mode access", "switchport access vlan 10"]
cmd_list2 = [
    "interface Gi0/2",
    "switchport mode trunk",
    "switchport trunk allowed vlan 10,20,30",
]
all_cmd_list = ["conf t", *cmd_list1, *cmd_list2, "end"]
pprint(all_cmd_list)


# dict and **

dict1 = {"hostname": "PE_R1", "Vendor": "Cisco", "ip": "10.1.1.1"}
new_dict = {"location": "London", **dict1}
pprint(new_dict)

dict1 = {"hostname": "PE_R1", "Vendor": "Cisco", "ip": "10.1.1.1"}
dict2 = {"ip": "10.1.1.100", "location": "London"}
new_dict = {**dict1, **dict2}
pprint(new_dict)
