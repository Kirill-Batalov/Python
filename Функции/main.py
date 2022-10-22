# Функция
def printSeq1(a, b):
    for i in range(a, b + 1):
        print(i, end=' ')


printSeq1(5, 100)


# Функция с параметром по-умолчанию
# Если step не передаётся, то принимается значение 1
def printSeq2(a, b, step=1):
    for i in range(a, b + 1, step):
        print(i, end=' ')


printSeq2(5, 100, 6)


# Функция с именованным параметром
# Если step не передаётся, то принимается значение 1
# * - После знака звёздочки идут именованные параметры
def printSeq3(a, b, sep=' ', *, step=1):
    for i in range(a, b + 1, step):
        print(i, end=sep)


printSeq3(5, 100, '->', step=2)
