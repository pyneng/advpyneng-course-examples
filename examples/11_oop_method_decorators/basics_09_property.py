import telnetlib
import time
import re


class CiscoTelnet:
    def __init__(self, ip, username, password, secret):
        print("__init__")
        self.ip = ip
        self._mngmt_ip = None
        self._config = None
        self._telnet = telnetlib.Telnet(ip)
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

    def _write_line(self, line):
        self._telnet.write(line.encode("utf-8") + b"\n")

    def send_show_command(self, command):
        self._write_line(command)
        command_output = self._telnet.read_until(b"#").decode("utf-8")
        return command_output

    def __repr__(self):
        return f"<CiscoTelnet ip={self.ip}>"

    @property
    def config(self):
        if not self._config:
            self._config = self.send_show_command("sh run | i hostname")
        return self._config

    @property
    def mngmt_ip(self):
        if not self._mngmt_ip:
            output = self.send_show_command("sh run int Loopback 0")
            match = re.search("ip address (\S+)", output)
            if match:
                self._mngmt_ip = match.group(1)
        return self._mngmt_ip

    @mngmt_ip.setter
    def mngmt_ip(self, new_ip):
        if new_ip != self._mngmt_ip:
            self.send_config_commands(
                ["interface loop0", f"ip address {new_ip} 255.255.255.255"]
            )
            self._mngmt_ip = new_ip

    def send_config_commands(self, commands):
        if type(commands) == str:
            commands = [commands]
        output = ""
        commands = ["conf t", *commands, "end"]
        for command in commands:
            self._telnet.write(command.encode("utf-8") + b"\n")
            output += self._telnet.read_until(b"#").decode("utf-8")
        return output

    def close(self):
        self._telnet.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._telnet.close()
