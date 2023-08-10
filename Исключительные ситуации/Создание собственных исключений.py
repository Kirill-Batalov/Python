class SideTriangleException(Exception):
    def __str__(self):
        return "Невозможно создать треугольник с данными сторонами"


class Triangle:
    def __init__(self, a, b, c):
        if (a + b) < c or (a + c) < b or (c + b) < a:
            raise SideTriangleException()
        self.a = a
        self.b = b
        self.c = c


try:
    t1 = Triangle(1, 12, 2)
except SideTriangleException as e:
    print(e)
