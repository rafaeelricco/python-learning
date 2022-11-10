# 🌎 Global Scope and Local Scope: basicallly, global scope is the scope of the entire program, and local scope is the scope of a function or a class.

x = 'John Doe'


def func(name):
    global x
    x = 'Jane Doe'
    print(f'Hello {name}')
