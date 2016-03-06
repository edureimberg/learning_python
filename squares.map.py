#Forma tradicional

squares = []
for n in range(10):
    squares.append(n ** 2)

print(squares)

#Usando lambda

squares2 = list(map(lambda m: m ** 2, range(10)))

print(squares2)
