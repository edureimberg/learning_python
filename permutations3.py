from itertools import permutations
from math import factorial

lista = 'ABC'

print(list(permutations(lista)))
print('São', factorial(len(lista)), 'possibilidades')
