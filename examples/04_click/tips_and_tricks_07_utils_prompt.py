import ipaddress
from pprint import pprint
import click


class ClickIPv4Address(click.ParamType):
    def convert(self, value, param, ctx):
        # print(f"{value=} {param=} {ctx=}")
        try:
            ipaddress.ip_address(value)
            return value
        except ValueError:
            self.fail(f"'{value}' is not a valid IP address")


# username = click.prompt("Введите имя пользователя")
# pprint(username)

# vlan = click.prompt("Введите номер влана", type=int)
# pprint(vlan)

# vlan = click.prompt("Введите номер влана", type=click.IntRange(1, 10))
# pprint(vlan)

# vlan = click.prompt("Введите номер влана", default=100)
# pprint(vlan)

# password = click.prompt("Введите пароль", hide_input=True)
# pprint(password)

# ip = click.prompt("Введите IP", type=ClickIPv4Address())
# pprint(ip)
