# Функции и способы чтения файлов подбираются в зависимости от структуры файла

# Обычный способ работы с файлами
"""
f = open('input1.txt')
<Операторы работы с файлами>
f.close()
"""

# Более профессиональный способ работы с файлами
# Не требует закрытия файла в конце работы с ним
with open('input1.txt') as f:
    # read() - функция, читающая весь файл в виде строки
    text = f.read()
    print(text)

