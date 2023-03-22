import re
import time
import telnetlib
from pprint import pprint

from textfsm import clitable
from textfsm.clitable import CliTableError


def parse_show(
    command, command_output, index_file="index", templates="templates"
):
    attributes = {"Command": command}
    cli_table = clitable.CliTable(index_file, templates)
    try:
        cli_table.ParseCmd(command_output, attributes)
    except CliTableError:
        return command_output
    else:
        return [dict(zip(cli_table.header, row)) for row in cli_table]


class CiscoTelnet:
    def __init__(self, host, username, password, secret):
        print("__init__")
        self.host = host
        self._mngmt_ip = None
        self._config = None
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

    def close(self):
        self._telnet.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._telnet.close()

    def __repr__(self):
        return f"<CiscoTelnet host={self.host}>"

    def _write_line(self, line):
        self._telnet.write(line.encode("utf-8") + b"\n")

    def send_show_command(self, command, parse=False):
        self._write_line(command)
        command_output = (
            self._telnet.read_until(b"#").decode("utf-8").replace("\r\n", "\n")
        )
        if parse:
            return self._parse_show(command, command_output)
            # return parse_show(command, command_output)
        else:
            return command_output

    _parse_show = staticmethod(parse_show)


if __name__ == "__main__":
    r1_params = {
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    with CiscoTelnet(**r1_params) as r1:
        pprint(r1.send_show_command("sh ip int br", parse=True), width=120)
        # pprint(r1.send_show_command("sh int desc", parse=True), width=120)

        # output = r1.send_show_command("sh ip int br")
    # pprint(CiscoTelnet._parse_show("sh ip int br", output), width=120)
