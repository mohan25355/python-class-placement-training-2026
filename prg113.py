def myfun(n):
    return lambda a : a*n
my=myfun(2)
print(my(5))