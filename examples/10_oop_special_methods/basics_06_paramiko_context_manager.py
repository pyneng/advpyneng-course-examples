import time
from pprint import pprint
import re

import paramiko


class CiscoSSH:
    def __init__(
        self,
        host,
        username,
        password,
        enable_pass,
        max_read=60000,
        pause=0.5,
    ):
        self.host = host
        self.username = username
        self.password = password
        self.max_read = max_read
        self.pause = pause

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
        self._ssh.settimeout(2)

        self._ssh.send("enable\n")
        self._ssh.send(f"{enable_pass}\n")
        time.sleep(self.pause)
        self._ssh.recv(self.max_read)
        self._ssh.send("terminal length 0\n")
        time.sleep(self.pause)
        read_output = self._ssh.recv(self.max_read).decode("utf-8")

    def send_show_command(self, command):
        self._ssh.send(f"{command}\n")
        time.sleep(self.pause)
        b_output = self._ssh.recv(self.max_read)
        output = b_output.decode("utf-8").replace("\r\n", "\n")
        return output

    def close(self):
        self._ssh.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


if __name__ == "__main__":
    # r1 = CiscoSSH("192.168.100.1", "cisco", "cisco", "cisco")
    # out = r1.send_show_command("sh clock")
    # pprint(out)
    # r1.close()

    with CiscoSSH("192.168.100.1", "cisco", "cisco", "cisco") as r1:
        out = r1.send_show_command("sh clock")
        pprint(out)
