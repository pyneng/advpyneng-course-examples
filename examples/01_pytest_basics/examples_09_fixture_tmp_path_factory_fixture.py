from pprint import pprint


def generate_access_config(intf_vlan_dict, access_template, output_cfg):
    with open(output_cfg, "w") as f:
        for intf, vlan in intf_vlan_dict.items():
            f.write(f"interface {intf}\n")
            for command in access_template:
                if command.endswith("access vlan"):
                    command = f"{command} {vlan}"
                f.write(f"{command}\n")


access_dict = {"FastEthernet0/12": 10, "FastEthernet0/14": 11}
cmd_list = ["switchport mode access", "switchport access vlan"]
generate_access_config(access_dict, cmd_list, "output1.txt")

access_dict = {
    "FastEthernet0/3": 100,
    "FastEthernet0/7": 101,
    "FastEthernet0/10": 111,
}

cmd_list = [
    "switchport mode access",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

generate_access_config(access_dict, cmd_list, "output2.txt")

def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
    assert 0
