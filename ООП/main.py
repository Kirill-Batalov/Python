# Класс - описание объекта
from math import sqrt


class Point:
    # Конструктор - функция, которая вызывается при создании экземпляра класса
    def __init__(self, x, y):
        # '_' - знак нижнего подчёркивания используется для создания private-переменных
        self.x = x
        self.y = y

    def get_distance(self, point):
        return sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)

    def distance_to_center(self):
        return self.get_distance(Point(0, 0))


p1 = Point(1, 1)
p2 = Point(2, 2)

print(p1.get_distance(p2))
print(p1.distance_to_center())

"""
    Создать класс Date для работы с датами.
    Конструктор принимает на вход строку вида дд.мм.гггг
    Добавить в класс операцию увеличения даты на один день (все правила календаря).
    
"""