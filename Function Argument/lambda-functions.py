# λ Lambda Functions: Basically, a lambda function is a small anonymous function.

def x(a): return a + 10


print(x(5))

# Output: 15


def x(a, b, c): return a + b + c


print(x(5, 6, 2))

# Output: 13


def myfunc(n):
    return lambda a: a * n


print(myfunc(2)(11))

# Output: 22
