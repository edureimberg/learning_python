from itertools import permutations

lista = 'eduardo'

num = 1
n = len(lista)

while n >= 1:
    num = num * n
    n -= 1

print(list(permutations(lista)))
print('São', num, 'combinações possíveis')
