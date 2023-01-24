from pprint import pprint
import re
import time
import paramiko


class CiscoSSH:
    def __init__(
        self,
        host,
        username,
        password,
        secret=None,
        pause=0.2,
        max_read=100000,
        read_timeout=2,
    ):
        self.host = host
        self.pause = pause
        self.max_read = max_read
        self.read_timeout = read_timeout

        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.connect(
            hostname=host,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False,
        )
        self._ssh = client.invoke_shell()
        self.prompt = self.get_prompt()
        self._send_command("terminal length 0")
        self._read_until("[>#]")
        if secret and "#" not in self.prompt:
            self._send_command("enable")
            self._read_until("Password")
            self._send_command(secret)
            self._read_until("#")
            self.prompt = self.get_prompt()

    def get_prompt(self):
        self._send_command("sh clock")
        time.sleep(self.pause)
        output = self._read_until("[#>]")
        match = re.search(r"\S+[>#]", output)
        if match:
            return match.group()
        else:
            raise ValueError("Couldn't find a prompt")

    def _send_command(self, command):
        self._ssh.send(f"{command}\n")

    def _read_until_prompt(self):
        output = self._read_until(self.prompt)
        return output

    def _read_until(self, regex):
        self._ssh.settimeout(self.read_timeout)
        output = ""
        while True:
            time.sleep(self.pause)
            try:
                part = self._ssh.recv(self.max_read).decode("utf-8")
                output += part
            except OSError:
                break
            match = re.search(regex, output)
            if match:
                break
        return output

    def send_show_command(self, show_command):
        self._send_command(show_command)
        output = self._read_until_prompt()
        return output

    def send_config_commands(self, commands):
        if type(commands) == str:
            commands = ["conf t", commands, "end"]
        else:
            commands = ["conf t", *commands, "end"]
        output = ""
        for cmd in commands:
            self._send_command(cmd)
            time.sleep(self.pause)
        output += self._read_until_prompt()
        return output

    def close(self):
        self._ssh.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


if __name__ == "__main__":
    with CiscoSSH(
        host="192.168.100.1", username="cisco", password="cisco", secret="cisco"
    ) as r1:
        print(r1.send_show_command("sh ip int br"))
        print(r1.send_config_commands("logging 5.5.5.5"))
        print(r1.send_show_command("sh run | i ^logging"))

    with CiscoSSH(host="192.168.100.1", username="cisco", password="cisco") as r1:
        print(r1.send_show_command("sh clock"))
        print(r1.send_show_command("sh ip int br"))
