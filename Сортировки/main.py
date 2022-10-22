list = [78, 55, 100, 654, 1, 0, 41, 44, 8, 99]

# Сортировка, изменяющая массив (модифицирующая сортировка)
# list.sort()

# Сортировка, не изменяющая массив, а возвращающая отсортированный
# list = sorted(list)

# Сортировка по убыванию
# list.sort(reverse=True)

# Сортировка чисел по кол-ву цифр
# list.sort(key=lambda o: len(str(o)))

# Сортировка по сумме цифр
list.sort(key=lambda o: sum(map(int, str(o))))

print(list)

# Info: https://docs.python.org/3/howto/sorting.html
