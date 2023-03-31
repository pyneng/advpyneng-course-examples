from rich import print


class Base:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<{type(self).__name__} {self.name}>"


class Parent1:
    def __init__(self, name, color="green"):
        self.name = name
        self.color = color

    def info(self):
        print("Parent1.info")
        print(f"[{self.color}]Parent1 {name}")


class Parent2:
    def __init__(self, name, upper=True):
        self.name = name.upper() if upper else name
        self.upper = upper

    def info(self):
        print("Parent2.info")
        print(f"Parent2 {self.name}")
