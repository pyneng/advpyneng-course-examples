from scrapli import Scrapli
import logging

logging.basicConfig(
    level=logging.INFO,
    format="{asctime} {levelname:10} {name:20} {host} {message}",
    style="{",
    datefmt="%H:%M:%S"
)

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
        logging.info(conn.get_prompt(), extra={'host': r1["host"]})
        print(conn.send_command("show run | i hostname").result)
