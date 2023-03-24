

class Number:
    def __set_name__(self, owner, name):
        print("__set_name__")
        self.attr_name = "_" + name

    def __get__(self, instance, cls):
        print("__get__")
        return getattr(instance, self.attr_name)

    def __set__(self, instance, value):
        print("__set__")
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        if value < 0:
            raise ValueError("Значение должно быть положительным")
        setattr(instance, self.attr_name, value)


class Book:
    price = Number()
    quantity = Number()

    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

