
class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    @property
    def mask(self):
        print("get_mask")
        return self._mask

    # mask = property(mask)

    @mask.setter
    def mask(self, new_mask):
        print("set_mask")
        if not isinstance(new_mask, int):
            raise TypeError("Маска должна быть числом")
        if new_mask not in range(0, 33):
            raise ValueError("Значение маски должно быть от 0 до 32")
        self._mask = new_mask

    # mask = mask.setter(mask)
