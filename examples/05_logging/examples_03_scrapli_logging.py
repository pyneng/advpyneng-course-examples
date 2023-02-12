from scrapli import Scrapli
from scrapli.logging import enable_basic_logging


enable_basic_logging(file="scrapli.log", level="info")

r1 = {
    "host": "192.168.100.1",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False,
    "platform": "cisco_iosxe",
    "auth_secondary": "cisco",
    "transport": "paramiko",
    "timeout_socket": 5,
    "timeout_transport": 10,
}


if __name__ == "__main__":
    with Scrapli(**r1) as conn:
        print(conn.get_prompt())
        print(conn.send_command("show run | i hostname").result)
