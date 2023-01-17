from pprint import pprint


def generate_access_config(intf_vlan_dict, access_template, output_cfg):
    with open(output_cfg, "w") as f:
        for intf, vlan in intf_vlan_dict.items():
            f.write(f"interface {intf}\n")
            for command in access_template:
                if command.endswith("access vlan"):
                    command = f"{command} {vlan}"
                f.write(f"{command}\n")


def test_generate_access_config_1(tmp_path):
    filename = tmp_path / "output.txt"
    access_dict = {"FastEthernet0/12": 10, "FastEthernet0/14": 11}
    cmd_list = ["switchport mode access", "switchport access vlan"]
    correct_output = (
        "interface FastEthernet0/12\n"
        "switchport mode access\n"
        "switchport access vlan 10\n"
        "interface FastEthernet0/14\n"
        "switchport mode access\n"
        "switchport access vlan 11\n"
    )
    generate_access_config(access_dict, cmd_list, filename)
    assert filename.read_text() == correct_output


def test_generate_access_config_2(tmp_path):
    filename = tmp_path / "output.txt"
    access_dict = {"FastEthernet0/7": 101, "FastEthernet0/10": 111}
    cmd_list = [
        "switchport mode access",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ]
    correct_output = (
        "interface FastEthernet0/7\n"
        "switchport mode access\n"
        "spanning-tree portfast\n"
        "spanning-tree bpduguard enable\n"
        "interface FastEthernet0/10\n"
        "switchport mode access\n"
        "spanning-tree portfast\n"
        "spanning-tree bpduguard enable\n"
    )
    generate_access_config(access_dict, cmd_list, filename)
    assert filename.read_text() == correct_output
