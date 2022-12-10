import random

matrix = [[random.randint(-10, 10) for j in range(10)] for i in range(10)]

# Улучшенный способ
for rows in matrix:
    # * - извлечение элементов из массива
    print(*rows, sep='\t')

# Обычный способ
for rows in matrix:
    for num in rows:
        # < - выравнивание по левому краю
        # 4 - 4 символа на каждое число
        print(f'{num:<4d}', end='')
    print()
# ПРИВЕТ КИРИЛЛ