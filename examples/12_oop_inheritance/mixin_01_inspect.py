from rich import inspect

class InspectMixin:
    def inspect(self, cls=False, **kwargs):
        """kwargs rich.inspect args"""
        if cls:
            inspect(type(self), **kwargs)
        else:
            inspect(self, **kwargs)


class IPAddress(InspectMixin):
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    def __repr__(self):
        return f"IPAddress({self.ip}/{self.mask})"

    def bin_mask(self):
        return "1" * self.mask + "0" * (32 - self.mask)
