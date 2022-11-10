# 🫳🏼 Handling Exceptions: Handling exceptions is a way to deal with errors that occur during execution of a program.

try:
    x = 1 / 0
except Exception as e:
    print(e)
finally:
    print('Finally')

# Output: division by zero
