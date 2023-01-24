from typing import Any


def request(host: str, url: str, port: int = 8080, protocol: str = "TCP") -> str:
    return f"{host}:{protocol}:{port}:{url}"


def get(host: str, **kwargs: Any) -> str:
    return request(host, **kwargs)


if __name__ == "__main__":
    print(get("10.1.1.1", url="google.com"))

