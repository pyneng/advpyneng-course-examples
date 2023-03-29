import time
from class_base_ssh import BaseSSH


class CiscoSSH(BaseSSH):
    def __init__(self, host, username, password, secret, **kwargs):
        super().__init__(host, username, password, **kwargs)
        self._send_and_read("terminal length 0")
        self._send_line("enable")
        self._send_and_read(secret)

    def send_config_commands(self, commands):
        if isinstance(commands, str):
            commands = ["conf t", commands, "end"]
        else:
            commands = ["conf t", *commands, "end"]
        result = super().send_config_commands(commands)
        return result

    def _read_until_prompt(self, prompt="#"):
        output = ""
        self._ssh.settimeout(1)
        while True:
            try:
                time.sleep(self.pause)
                part = self._ssh.recv(self.max_read).decode("utf-8")
                output += part
                if prompt in output:
                    break
            except OSError:
                break
        return output

    def _send_and_read(self, command):
        print(f"CiscoSSH _send_and_read {command=}")
        self._send_line(command)
        output = self._read_until_prompt()
        return output




if __name__ == "__main__":
    with CiscoSSH("192.168.100.1", "cisco", "cisco", "cisco") as r1:
        print(r1.send_show_command("sh clock"))
        print(r1.send_config_commands("int loop 945"))

