import re
import time
import telnetlib
from pprint import pprint


class CiscoTelnet:
    def __init__(self, host, username, password, secret):
        self.host = host
        self._telnet = telnetlib.Telnet(host)
        self._telnet.read_until(b"Username:")
        self._write_line(username)
        self._telnet.read_until(b"Password:")
        self._write_line(password)
        self._write_line("enable")
        self._telnet.read_until(b"Password:")
        self._write_line(secret)
        self._write_line("terminal length 0")
        time.sleep(1)
        self._telnet.read_very_eager()

    @property
    def config(self):
        return self.send_show_command("sh run | i interface")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._telnet.close()

    def _write_line(self, line):
        self._telnet.write(line.encode("utf-8") + b"\n")

    def send_show_command(self, command):
        self._write_line(command)
        command_output = (
            self._telnet.read_until(b"#").decode("utf-8").replace("\r\n", "\n")
        )
        return command_output


if __name__ == "__main__":
    r1_params = {
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    with CiscoTelnet(**r1_params) as r1:
        pprint(r1.send_show_command("sh ip int br"), width=120)
