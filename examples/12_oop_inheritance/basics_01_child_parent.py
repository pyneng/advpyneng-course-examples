class Parent1:
    def __init__(self, name):
        print(f"Parent1 __init__ {self=")
        self.name = name

    def method1(self):
        print("Parent1 method1")

    def method2(self):
        print("Parent1 method2")
        self.method1()

