
class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self._mask = self._check_mask(mask)

    @property
    def mask(self):
        print("get_mask")
        return self._mask

    def _check_mask(self, new_mask):
        print("set_mask")
        if not isinstance(new_mask, int):
            raise TypeError("Маска должна быть числом")
        if new_mask not in range(0, 33):
            raise ValueError("Значение маски должно быть от 0 до 32")
        return new_mask
