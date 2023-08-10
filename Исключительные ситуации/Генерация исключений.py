class Triangle:
    def __init__(self, a, b, c):
        if (a + b) < c or (a + c) < b or (c + b) < a:
            raise Exception("Невозможно создать треугольник с данными сторонами")


try:
    t1 = Triangle(1, 12, 2)
except Exception as e:
    print(f'Ошибка!\n{e}')