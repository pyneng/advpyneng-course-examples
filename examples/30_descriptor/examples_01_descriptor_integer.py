class Integer:
    def __set_name__(self, owner, name):
        print(f"set_name {owner=} {attr_name=}")
        self.attr_name = "_" + name

    def __get__(self, instance, cls=None):
        print(f"__get__  {instance=} {cls=}")
        return getattr(instance, self.attr_name)

    def __set__(self, instance, value):
        print(f"__set__  {instance=} {value=}")
        if not isinstance(value, int):
            raise TypeError("Значение должно быть числом")
        if not value >= 0:
            raise ValueError("Значение должно быть положительным")
        setattr(instance, self.attr_name, value)


class Book:
    price = Integer()
    quantity = Integer()

    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity


