from pprint import pprint

DEVICE_TYPE_CLASS_MAP = {}


def register(cls):
    if not hasattr(cls, "device_type"):
        raise TypeError("Декоратор работает только с классами с атрибутом device_type")
    DEVICE_TYPE_CLASS_MAP[cls.device_type] = cls
    return cls


# @register
class CiscoIosBase:
    pass


@register
class CiscoSSH(CiscoIosBase):
    device_type = "cisco_ios"

    def __init__(self, ip, user, password):
        pass


@register
class JuniperSSH:
    device_type = "juniper"

    def __init__(self, ip, user, password):
        pass


# JuniperSSH = register(JuniperSSH)


pprint(DEVICE_TYPE_CLASS_MAP)
