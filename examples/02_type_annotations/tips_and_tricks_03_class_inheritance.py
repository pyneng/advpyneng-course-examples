from typing import Iterable


class BaseSSH:
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
    ):
        pass

    def send_show_command(self, show_command: str) -> str:
        return f"{show_command}"

    def send_config_commands(self, commands: str | Iterable[str]) -> str:
        return "commands"


class CiscoSSH(BaseSSH):
    def send_show_command(self, show_command: str, timeout: int) -> str:
        return f"{show_command}"

    def send_config_commands(self, commands: str | list[str]) -> str:
        return "commands"

if __name__ == "__main__":
    r1 = CiscoSSH(host="192.168.100.1", username="cisco", password="cisco")
    print(r1.send_show_command("sh ip int br", timeout=10))

    r2 = BaseSSH(host="192.168.100.1", username="cisco", password="cisco")
    print(r2.send_show_command("sh ip int br"))

# $ mypy basics_17_class_inheritance.py  --strict
# basics_17_class_inheritance.py:21: error: Signature of "send_show_command" incompatible with supertype "BaseSSH"  [override]
# basics_17_class_inheritance.py:21: note:      Superclass:
# basics_17_class_inheritance.py:21: note:          def send_show_command(self, show_command: str) -> str
# basics_17_class_inheritance.py:21: note:      Subclass:
# basics_17_class_inheritance.py:21: note:          def send_show_command(self, show_command: str, timeout: int) -> str
# basics_17_class_inheritance.py:24: error: Argument 1 of "send_config_commands" is incompatible with supertype "BaseSSH"; supertype defines the argument type as "Union[str, Iterable[str]]"  [override]
# basics_17_class_inheritance.py:24: note: This violates the Liskov substitution principle
# basics_17_class_inheritance.py:24: note: See https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
# Found 2 errors in 1 file (checked 1 source file)
# 
