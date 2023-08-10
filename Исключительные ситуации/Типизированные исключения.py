"""
    Пример некоторых исключений
    (остальные можно смотреть в pycharm во время работы, либо в документации)
    BaseException - базовый тип всех исключений
    ArithmeticError - базовый тип арифметических исключений
        OverflowError
        ZeroDivisionError
        FloatingPointError
        ...
    RecursionError - переполнение стека вызовов рекурсии
    ValueError - ошибка, связанная с типами
    IndexError - ошибка обращения к индексам коллекций
"""

try:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    print(f'Частное от деления {number1} на {number2} = {number1 / number2}')
except ValueError:
    print('Вы ввели не число!')
except ZeroDivisionError:
    print('Упс... деление на ноль')
