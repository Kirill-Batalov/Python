list = list(map(int, input().split()))
size = len(list)
i = 0
while i < size:
    if list[i] == 0:
        list.pop(i)
        list.append(0)
        size -= 1
    if list[i] != 0:
        print(list[i], end=' ')
        i += 1
print("0 " * (len(list) - size))

