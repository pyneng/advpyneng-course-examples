from collections import namedtuple


Stock = namedtuple('Stock', 'name price shares')
s = Stock('AAPL', 750.34, 90)

%%timeit
value = s.price * s.shares


class Stock2:
    __slots__ = ('name', 'price', 'shares')
    def __init__(self, name, price, shares):
        self.name = name
        self.price = price
        self.shares = shares
s2 = Stock2('AAPL', 750.34, 90)
%%timeit
value = s2.price * s2.shares
class Stock3:
    def __init__(self, name, price, shares):
        self.name = name
        self.price = price
        self.shares = shares
s3 = Stock3('AAPL', 750.34, 90)
%%timeit
value = s3.price * s3.shares
t = ('AAPL', 750.34, 90)
%%timeit
values = t[1] * t[2]
d = dict(name='AAPL', price=750.34, shares=90)
%%timeit
value = d['price'] * d['shares']

