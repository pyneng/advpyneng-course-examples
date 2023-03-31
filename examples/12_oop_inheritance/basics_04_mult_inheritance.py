from rich import print


class Base:
    def __init__(self, name):
        self.name = name


class Parent1:
    def __init__(self, name, color="green"):
        self.name = name
        self.color = color

    def info(self):
        print("Parent1.info")

    def method1(self):
        print(f"[{self.color}]Parent1 method1")


class Parent2:
    def __init__(self, name, upper=True):
        self.name = name
        self.upper = upper

    def info(self):
        print("Parent2.info")

    def method2(self):
        name = self.name.upper() if self.upper else self.name
        print(f"Parent2 method2 {name}")
