from rich import inspect


def _inspect(self, cls=False, methods=False, dunder=False):
    if cls:
        inspect(type(self), methods=methods)
    else:
        inspect(self, methods=methods)


def add_inspect(cls):
    cls.inspect = _inspect
    return cls


@add_inspect
class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    def __repr__(self):
        return f"IPAddress({self.ip}/{self.mask})"

    def bin_mask(self):
        return "1" * self.mask + "0" * (32 - self.mask)
