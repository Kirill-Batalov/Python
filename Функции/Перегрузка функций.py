'''
# Способ, не требующий никаких дополнительных библиотек
def f(point=None):
    if point == None:
        print([0, 0])
    else:
        print(point)

f()
'''


# --- Multiple Dispatch ---

from multipledispatch import dispatch


@dispatch(int, int, int)
def check_date(day: int, month: int, year: int):
    return "1"


@dispatch(str)
def check_date(date: str):
    return "2"


print(check_date(5, 7, 85))

# --- Single Dispatch ---

from functools import singledispatch


@singledispatch
def length(num):
    return 0


@length.register
def _(num: int):
    return len(str(num))


@length.register
def _(num: str):
    return len(num)


print(length("4.5"))
