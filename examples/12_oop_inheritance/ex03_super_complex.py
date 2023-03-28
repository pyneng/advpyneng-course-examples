class Base:
    def info(self):
        print("Base.info")


class Parent1(Base):
    def info(self):
        print("Parent1.info")
        super().info()


class Parent2(Base):
    def info(self):
        print("Parent2.info")
        super().info()


class Child(Parent1, Parent2):
    pass


# Child ----> Parent1 ---+
#     |                  |--> Base
#     +-----> Parent2 ---+

c1 = Child()
c1.info()
print(Child.mro())
