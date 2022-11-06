size = int(input())

matrix = [[0 if i == j or size - 1 - i == j else
           3 if i > j > size - 1 - i else
           2 if j > i and size - 1 - i < j else
           1 if i < j < size - 1 - i else
           4 for j in range(size)] for i in range(size)]

for rows in matrix:
    print(*rows, sep='\t')