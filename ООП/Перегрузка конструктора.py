from multipledispatch import dispatch

# I способ
class Date:
    @dispatch(int, int, int)
    def __init__(self, day: int, month: int, year: int):
        self.day, self.month, self.year = day, month, year
        print("int, int, int")

    @dispatch(str)
    def __init__(self, date: str):
        self.day, self.month, self.year = map(int, date.split())
        print("str")


# II способ
class Date:
    def __init__(self, *args):
        if len(args) == 1:
            self.day, self.month, self.year = map(int, args[0].split())
        if len(args) == 3:
            self.day, self.month, self.year = args[0], args[1], args[2]
