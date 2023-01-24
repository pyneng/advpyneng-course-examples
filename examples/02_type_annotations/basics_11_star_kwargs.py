

def request(host: str, url: str, protocol: str = "TCP") -> str:
    return f"{host}:{protocol}:{url}"


def get(host: str, **kwargs: str) -> str:
    print(kwargs)
    reveal_type(kwargs)
    return request(host, **kwargs)


if __name__ == "__main__":
    print(get("10.1.1.1", url="google.com"))

