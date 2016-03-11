def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

squares = get_squares_gen(3)
print(squares.__next__())
print(squares.__next__())
print(squares.__next__())
print(squares.__next__())        
