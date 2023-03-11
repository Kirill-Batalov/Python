class Student:
    def __init__(self, full_name, group, birth_date):
        self._full_name = full_name
        self._group = group
        self._birth_date = birth_date

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        self._full_name = full_name


s1 = Student('Пупкин Иван', 'АСУ-5', '2002-12-03')

s1.full_name = 'Пупкин Александр'

print(s1.full_name)

