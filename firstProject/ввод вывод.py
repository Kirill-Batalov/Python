# input - функция, получающая строку с клавиатуры
# int - функция, преобразующая в целое число
width = int(input('Введите w: '))
height = int(input('Введите h: '))

# Форматированный вывод (f'')
print(f'Периметр = {(width + height) * 2}')
print(f'Площадь = {width * height}')