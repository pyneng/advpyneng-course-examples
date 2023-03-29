class Parent1:
    def __init__(self, name):
        print(f"Parent1 __init__ {self=}")
        self.name = name

    def method1(self):
        print("Parent1 method1")

    def method2(self):
        print("Parent1 method2")
        self.method1()


class Child(Parent1):
    def method3(self):
        print("Child method3")
