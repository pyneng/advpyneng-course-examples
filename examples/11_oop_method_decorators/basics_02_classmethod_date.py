class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"Date({self.day}, {self.month}, {self.year})"

    @classmethod
    def from_str(cls, date_as_str):
        print(f"{cls=}")
        day, month, year = map(int, date_as_str.split("/"))
        return cls(day, month, year)


if __name__ == "__main__":
    d1 = Date(22, 11, 2022)
    print(d1)
    d2 = Date.from_str("22/11/2022")
    print(d2)

