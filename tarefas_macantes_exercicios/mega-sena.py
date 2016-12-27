import random

num = []

for i in range(1,7):
    num.append(random.randint(1,60))

num.sort()

print(num)