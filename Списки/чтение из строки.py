# На вход подаётся строка, состоящая из чисел
# 456 888 633 221 32
# Как получить массив чисел????????????????????????

# split - функция, разделяет строку на части. Разделителем является пробел по-умолчанию.
# map   - функция, которая применяет к последовательности какую-либо функцию.
#         Например, в нашем случае, к элементам применяется функция int

inp = input().split()
list = map(int, inp)
# sum - функция, суммирующая массив
print(sum(list))