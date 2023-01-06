import telnetlib


def get_output(
    ip, username, password, command, enable_password=None, disable_paging=True
):
    def send_command(command, prompt=b"#"):
        telnet.write(command.encode("ascii") + b"\n")
        output = telnet.read_until(prompt, timeout=5).decode("ascii")
        return output

    with telnetlib.Telnet(ip) as telnet:
        telnet.read_until(b"Username:")
        send_command(username, prompt=b"Password:")
        send_command(password, prompt=b">")
        if enable_password:
            send_command("enable", prompt=b"Password:")
            send_command(enable_password)
        if disable_paging:
            send_command("terminal length 0")
        output = send_command(command)
    return output


if __name__ == "__main__":
    out = get_output(
        "192.168.100.1",
        "cisco",
        "cisco",
        command="sh ip int br",
        enable_password="cisco",
    )
    print(out)
