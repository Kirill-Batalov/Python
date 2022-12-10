# Словарь
# { {ключ: значение}, ... }
# Ключи не могут повторяться
stat = {}
line = input().lower()
for c in line:
    # Если в словаре уже имеется такой ключ
    if c in stat:
        stat[c] += 1
    else:
        stat[c] = 1

# Сортировка словаря по ключам
stat = dict(sorted(stat.items()))

for key, value in stat.items():
    print(f'{key} - {value}')
