# 🎭 args & **kwargs
# unpacking arguments

def func(*args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, 3, 4, 5, name="John", age=36)
