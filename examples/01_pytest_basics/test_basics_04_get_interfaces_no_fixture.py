from basics_02_get_interfaces import get_interfaces_from_cfg

def test_only_phy():
    input_cfg = (
        "!\n"
        "interface FastEthernet0/0\n"
        " ip address 10.1.1.1 255.255.255.0\n"
        "!\n"
        "interface FastEthernet0/1\n"
        " no ip address\n"
        "!\n"
        "interface FastEthernet0/2\n"
        " ip address 10.2.2.2 255.255.255.0\n"
        "!\n"
    )
    correct_intf_list = ["FastEthernet0/0", "FastEthernet0/1", "FastEthernet0/2"]
    intf_list = get_interfaces_from_cfg(input_cfg)
    assert intf_list == correct_intf_list


def test_only_phy_and_loopback():
    input_cfg = (
        "!\n"
        "interface FastEthernet0/0\n"
        " ip address 10.1.1.1 255.255.255.0\n"
        "!\n"
        "interface FastEthernet0/1\n"
        " no ip address\n"
        "!\n"
        "interface FastEthernet0/2\n"
        " description test\n"
        " ip address 10.2.2.2 255.255.255.0\n"
        "!\n"
        "interface Loopback100\n"
        " description test\n"
        " ip address 10.100.255.2 255.255.255.0\n"
    )
    correct_intf_list = ["FastEthernet0/0", "FastEthernet0/1", "FastEthernet0/2", "Loopback100"]
    intf_list = get_interfaces_from_cfg(input_cfg)
    assert intf_list == correct_intf_list


def test_empty_cfg():
    input_cfg = ""
    correct_intf_list = []
    intf_list = get_interfaces_from_cfg(input_cfg)
    assert intf_list == correct_intf_list
