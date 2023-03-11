# Декоратор
def logo(func):
    def print_logo(n):
        print("Repka")
        func(n)
    return print_logo


@logo
def print_seq(n):
    for i in range(n):
        print(i, end=' ')


print_seq(10)