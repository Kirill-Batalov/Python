class Person:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def get_age(self):
        # Реализация...
        return 0


# Наследование от класса Person
class Student(Person):
    def __init__(self, first_name, last_name, birth_date, admission_year):
        # Вызов конструктора базового класса
        super().__init__(first_name, last_name, birth_date)
        self.admission_year = admission_year


class Lecturer(Person):
    def __init__(self, first_name, last_name, birth_date, subject):
        super().__init__(first_name, last_name, birth_date)
        self.subject = subject

"""
    Geometry
    Реализовать структуру классов для работы с геометрическими фигурами на плоскости.
    Функционал:
    1. Определение площади
    2. Определение периметра
    Фигуры:
    Окружность, Квадрат, Прямоугольник, Треугольник, *Многоугольник
    Базовый класс - Shape
"""