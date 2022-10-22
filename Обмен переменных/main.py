a = 6
b = 12

print(f'a={a}, b={b}')
'''
c = a
a = b
b = c
'''
a, b = b, a
print(f'a={a}, b={b}')